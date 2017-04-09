telescope
=========

Tracking starred github repo's latest releases


telescope gets you a list of all releases (markdown formatted) from the last 8
days from all repositories you starred on github.

I run it via cron and get its output via email.

install
-------
telescope requires PyGithub_, python 3 and can be installed with::

  pip install .

configuration & usage
---------------------

Put your username and access token into the __init__.py file (before
installing) or set the environment variables `GH_USER` and `GH_TOKEN`:

  GH_USER=geier GH_TOKEN=c0ffee telescope

telescope will work without an authentication token for as long as github's
API allows it, but you might want to create_ one.


Example
-------

see the `example output <example_output.md>`_

.. _PyGithub: https://pypi.python.org/pypi/PyGithub
.. _create: https://github.com/blog/1509-personal-api-tokens
