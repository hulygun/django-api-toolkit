from setuptools import setup, find_packages
from os.path import join, dirname

import api_tools

__author__ = 'hulygun'

setup(
    name='django-api-toolkit',
    version=api_tools.__version__,
    author=api_tools.__author__,
    author_email=api_tools.__author_email__,
    url='https://github.com/hulygun/django-api-toolkit',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    entry_points={
        'console_scripts':
            [
                'project_init = api_tools.scripts:project_init',
                'env_generator = api_tools.scripts:env_generator'
            ]
    },
    install_requires=[r for r in open(join(dirname(__file__), 'api_tools', 'requirements.txt')).readlines()],
    test_suite='tests',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='api rest django',
    python_requires='>=3.5'

)
