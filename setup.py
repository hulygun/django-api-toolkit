from setuptools import setup, find_packages
from os.path import join, dirname

import api_tools

setup(
    name='django-api-tools',
    version=api_tools.__version__,
    author=api_tools.__author__,
    author_email=api_tools.__author_email__,
    url='https:github.org/hulygun/django-api-tools',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    entry_points={
        'console_scripts':
            ['project_init = api_tools.scripts:project_init']
    },
    install_requires=[r for r in open(join(dirname(__file__), 'api_tools', 'requirements.txt')).readlines()],
    test_suite='tests',
)
