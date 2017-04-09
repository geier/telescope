#!/usr/bin/env python3
"""Telescope -- looking for the stars.

Getting releases of starred github repos that occurred during the week.
"""

# Configuration
USER = 'geier'  # put your username here
TOKEN = False   # set this or create a file token.txt containing the access token
DAYS = 8        # getting releases for the last X days

import datetime as dt
import os
import logging

from github import Github

logging.basicConfig(level=logging.INFO)
NOW = dt.datetime.now()

def get_token():
    """Get the access token from file."""
    try:
        with open('token.txt') as f:
            token = f.readline().strip()
    except FileNotFoundError:
        logging.warning("no token found, unauthenticated might also work")
        token = None
    return token


def parse_date(string):
    return dt.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')


def format_repo(repo):
    out = list()
    out.append('')
    out.append(repo['name'])
    out.append('=' * len(repo['name']))
    out.append(repo['description'])
    out.append('https://github.com/{}/releases/'.format(repo['name']))
    for release in repo['releases']:
        out.append('')
        subheader = '{name} {tag_name} {published_at}'.format(**release)
        out.append(subheader)
        out.append('-' * len(subheader))
        # body is sometimes None
        text = release.get('body', "Tag release, no description") or ''
        out.extend(text.splitlines())

    return '\n'.join([str(one) for one in out])  # for some reasons, there are sometimes Nones in here


def main():
    user = os.environ.get('GH_USER') or USER
    logging.info("tracking stars for user {}".format(user))
    logging.info("If this is not your username, change it in the python file")
    user = Github(os.environ.get('GH_TOKEN') or TOKEN or get_token()).get_user(USER)

    for repo in user.get_starred():
        repo_ = {
            'name': repo.full_name,
            'description': repo.description,
            'releases': list(),
        }
        logging.info("getting {}".format(repo.full_name))
        for release in repo.get_releases():
            release_date = parse_date(release.raw_data['published_at'])
            if NOW - release_date < dt.timedelta(days=DAYS):
                repo_['releases'].append(release.raw_data)
            else:
                break  # TODO XXX we assume, that those releases are ordered
        for tag in repo.get_tags():
            sha = tag.raw_data['commit']['sha']
            commit = repo.get_commit(sha)
            tag_date = parse_date(commit.raw_data['commit']['author']['date'])
            if (NOW - tag_date < dt.timedelta(days=DAYS)):
                if tag.name not in [r['name'] for r in repo_['releases']]:
                    tag.raw_data['tag_name'] = ''
                    tag.raw_data['published_at'] = commit.raw_data['commit']['author']['date']
                    repo_['releases'].append(tag.raw_data)
            else:
                break
        if repo_['releases']:
            print(format_repo(repo_))


if __name__ == '__main__':
    main()
