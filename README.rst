Very simple app for REST API create via Django Framework
========================================================

.. image:: https://travis-ci.org/hulygun/django-api-toolkit.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/hulygun/django-api-toolkit

.. image:: https://img.shields.io/pypi/v/django-api-toolkit.svg
    :alt: pypi
    :target: https://pypi.org/project/django-api-toolkit/

.. image:: https://img.shields.io/pypi/pyversions/django-api-toolkit.svg
    :alt: python
    :target: https://pypi.org/project/django-api-toolkit/

.. image:: https://img.shields.io/pypi/l/django-api-toolkit.svg
    :alt: license
    :target: https://pypi.org/project/django-api-toolkit/

.. image:: https://img.shields.io/pypi/status/django-api-toolkit.svg
    :alt: Development status
    :target: https://pypi.org/project/django-api-toolkit/

.. image:: https://coveralls.io/repos/github/hulygun/django-api-toolkit/badge.svg?branch=master
    :target: https://coveralls.io/github/hulygun/django-api-toolkit?branch=master



.. contents::

Instalation
-----------
.. code-block:: bash

  pip install django-api-toolkit

Get started
-----------

In the first you need initialize your project

.. code-block:: bash

  project_init <path to project>

For existing projects you should to generate **env** file

.. code-block:: bash

  env_generator <path to project>

This script generate base variables that needed to run project. You can also add youself variables in env file
You should also change your **manage.py**. Add *APIManager* to your file. e.q.

.. code-block:: python

  #!/usr/bin/env python
  import sys

  from api_tools.utils import APIManager

  if __name__ == "__main__":
      er = APIManager(__file__, 'cfg.settings')  # path to user project settings
      er.set_app_dir('apps')  # directory for user project applications
      er.apply()  # apply settings

      from django.core.management import execute_from_command_line
      execute_from_command_line(sys.argv)


Usage
-----

Structure
~~~~~~~~~

.. code-block:: bash

  ├── apps  # dir for your apps
  ├── cfg  # dir for diferent project configurations
  │   ├── settings.py # user project settings
  │   └── wsgi.py
  └── manage.py


Settings
~~~~~~~~

- **COMMON_APPS** - django common applications
- **THIRD_PARTY_APPS** - third party applications
- **EXTRA_APPS** - applications should be insted before common apps
- **PROJECT_APPS** - your project applications

You also can overwrite other standard django settings keys and add yourself variables

Models
~~~~~~

All project models should be inherited of RestModel(this standart django abstract model and you can use all capabilities
of this)

.. code-block:: python

  from api_tools.models import RestModel

  class MyModel(RestModel):
      ...

Advanced
--------

**RestModel** have subclass **Rest**. This subclass have properties for control your rest models. RestModel also have
classmethods for these controls.


RestModel overwrites
~~~~~~~~~~~~~~~~~~~~

RestModel.Rest
..............

:queryset: defines queryset as **lambda** of :code:`model.objects`
:fields: list of allowed fields of model
:name: name of viewset
:route: route of endpoint

RestModel._rest_serializer
..........................

Defines serializer for viewset of model

RestModel._rest_queryset
........................

Defines queryset for viewset

RestModel._rest_endpoint
........................

Set endpoint for your model

FEATURES
--------

CHANGELOG
---------
