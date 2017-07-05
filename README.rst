Very simple app for REST API create via Django Framework
========================================================

Instalation
-----------
::

  pip install django-api-toolkit

Get started
-----------

In the first you need initialize your project::

  project_init <path to project>

For existing projects you should to generate **env** file::

  env_generator <path to project>

This script generate base variables that needed to run project. You can also add youself variables in env file
You should also change your **manage.py**. Add *APIManager* to your file. e.q. ::

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
::

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


