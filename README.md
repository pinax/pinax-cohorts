![](http://pinaxproject.com/pinax-design/patches/pinax-cohorts.svg)

# Pinax Cohorts

[![](https://img.shields.io/pypi/v/pinax-cohorts.svg)](https://pypi.python.org/pypi/pinax-cohorts/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-cohorts.svg)](https://circleci.com/gh/pinax/pinax-cohorts)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-cohorts.svg)](https://codecov.io/gh/pinax/pinax-cohorts)
[![](https://img.shields.io/github/contributors/pinax/pinax-cohorts.svg)](https://github.com/pinax/pinax-cohorts/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-cohorts.svg)](https://github.com/pinax/pinax-cohorts/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-cohorts.svg)](https://github.com/pinax/pinax-cohorts/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Templates](#templates)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-cohorts

### Overview

Create cohorts for inviting people off your pinax-waitinglist waiting list to
your private beta site.

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation

### Installation

To install pinax-cohorts:

```shell
    $ pip install pinax-cohorts
```

Add `pinax.cohorts` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.cohorts",
    ]
```

Add `pinax.cohorts.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^cohorts/", include("pinax.cohorts.urls", namespace="pinax_cohorts")),
    ]
```

### Templates

Default templates are provided by the `pinax-templates` app in the
[cohorts](https://github.com/pinax/pinax-templates/tree/master/pinax/templates/templates/pinax/cohorts)
section of that project.

Reference pinax-templates
[installation instructions](https://github.com/pinax/pinax-templates/blob/master/README.md#installation)
to include these templates in your project.

View live `pinax-templates` examples and source at [Pinax Templates](https://templates.pinaxproject.com/pinax-cohorts/)!

#### Customizing Templates

Override the default `pinax-templates` templates by copying them into your project
subdirectory `pinax/cohorts/` on the template path and modifying as needed.

For example if your project doesn't use Bootstrap, copy the desired templates
then remove Bootstrap and Font Awesome class names from your copies.
Remove class references like `class="btn btn-success"` and `class="icon icon-pencil"` as well as
`bootstrap` from the `{% load i18n bootstrap %}` statement.
Since `bootstrap` template tags and filters are no longer loaded, you'll also need to update
`{{ form|bootstrap }}` to `{{ form }}` since the "bootstrap" filter is no longer available.

#### `_members.html`

#### `_status.html`

#### `cohort_create.html`

#### `cohort_detail.html`

#### `cohort_list.html`


## Change Log

### 1.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 0.7

* Add expired field to Member, to show signup code has expired, if expiry date has passed

### 0.6

* Fix permission references

### 0.5

* Update pinax-waitinglist version requirement

### 0.4

* fix test urls
* fix import sorting

### 0.3

* Add django>=1.11 to installation requirements
* Update CI configuration
* Remove unused paths from MANIFEST
* Remove doc build support
* Remove unused files

### 0.2

* Update for Django 2.0 support

### 0.1

* Initial Release


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
