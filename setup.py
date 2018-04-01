#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='falcon-example',
    version='1.0.0',
    description=('Example '),
    long_description=desc,
    url='https://github.com/jmvrbanac/falcon-example',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=[
        'falcon>=1.4.1',
        'gunicorn>=19.6.0',
        'docopt>=0.6.2',
        'jsonschema>=2.5.1',
        'mysql-connector>=2.1.4',
        'sqlalchemy>=1.1.4',
        'aumbry[yaml]>=0.2.0'
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'falcon-example = example.__main__:main'
        ],
    },
)
