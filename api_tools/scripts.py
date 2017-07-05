import os
import random
import sys

FORMATER = '=' * 5
MANAGE_TEMPLATE = \
"""#!/usr/bin/env python
import sys

from api_tools.utils import APIManager

if __name__ == "__main__":
    er = APIManager(__file__, 'cfg.settings')
    er.set_app_dir('apps')
    er.apply()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
"""
SETTINGS_TEMPLATE = \
"""PROJECT_APPS = []
WSGI_APPLICATION = 'cfg.wsgi.application'
"""
WSGI_TEMPLATE = \
"""from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
"""


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def project_init():
    print('{formater} {bold}New project initialization{end} {formater}'.format(formater=FORMATER, bold=color.BOLD,
                                                                               end=color.END))

    project_path = get_project_path()
    print('Init project in ' + project_path)
    print('Create structure ...')
    os.makedirs(project_path, exist_ok=True)
    base_dirs = ['cfg', 'apps']
    for directory in base_dirs:
        os.makedirs(os.path.join(project_path, directory), exist_ok=True)

    with open(os.path.join(project_path, 'manage.py'), 'a') as manage_file:
        manage_file.write(MANAGE_TEMPLATE)

    with open(os.path.join(project_path, 'cfg', 'settings.py'), 'a') as settings_file:
        settings_file.write(SETTINGS_TEMPLATE)

    with open(os.path.join(project_path, 'cfg', 'wsgi.py'), 'a') as wsgi_file:
        wsgi_file.write(WSGI_TEMPLATE)

    env_generator()

    print('{formater} {bold}Initialization complete{end} {formater}'.format(formater=FORMATER, bold=color.BOLD,
                                                                            end=color.END))


def env_generator():
    print('Generate env file ...')
    project_path = get_project_path()
    with open(os.path.join(project_path, '.env'), 'a') as env_file:
        env_file.write('DEBUG={}\n'.format(input('DEBUG[on/off]? ')))
        env_file.write('SECRET_KEY={}\n'.format(secret_key_generator()))
        schemas = {1: 'sqlite', 2: 'mysql', 3: 'postgresql'}
        db_schema = int(input("""Choice DB schema:
        1. sqlite
        2. mysql
        3. postgresql
        
        """))

        db_name = input('Database name? ')
        db_string = '{}://'.format(schemas[db_schema])
        if db_schema > 1:
            db_user = input('Database user? ')
            if db_user:
                db_string += db_user
            db_pass = input('Database pass? ')
            if db_pass:
                db_string += ':{}'.format(db_pass)
            db_host = input('Database host? ')
            if db_host:
                db_string += '@{}'.format(db_host)
            db_port = input('Database port? ')
            if db_port:
                db_string += ':{}'.format(db_port)
        db_string += '/{}'.format(db_name)
        env_file.write('DATABASE_URL={}'.format(db_string))


def secret_key_generator():
    return ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])


def get_project_path():
    try:
        relative_path = sys.argv[1]
    except IndexError:
        relative_path = '.'
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))
