from setuptools import find_packages, setup

VERSION = "0.4"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-cohorts.svg
    :target: https://pypi.python.org/pypi/pinax-cohorts/

=============
Pinax Cohorts
=============

.. image:: https://img.shields.io/pypi/v/pinax-cohorts.svg
    :target: https://pypi.python.org/pypi/pinax-cohorts/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-cohorts.svg
    :target: https://circleci.com/gh/pinax/pinax-cohorts
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-cohorts.svg
    :target: https://codecov.io/gh/pinax/pinax-cohorts
.. image:: https://img.shields.io/github/contributors/pinax/pinax-cohorts.svg
    :target: https://github.com/pinax/pinax-cohorts/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-cohorts.svg
    :target: https://github.com/pinax/pinax-cohorts/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-cohorts.svg
    :target: https://github.com/pinax/pinax-cohorts/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT

\

Create cohorts for inviting people off your pinax-waitinglist waiting list to
your private beta site.


Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  2.0            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxprojects.com",
    description="Create cohorts for inviting people off your pinax-waitinglist waiting list to your private beta site.",
    name="pinax-cohorts",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-cohorts/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "cohorts": []
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=1.11",
        "django-user-accounts>=2.0.3",
        "pinax-waitinglist>=2.0.2"
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
