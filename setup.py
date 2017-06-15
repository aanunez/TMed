#!/usr/bin/env python3

from setuptools import setup

setup(
	name = 'TMed',
	version = '0.1',
	description = 'Edit and Restore the TM table on Gen 3 Pokemon Games',
	author = 'Adam Nunez',
	author_email = 'adam.a.nunez@gmail.com',
	license = 'GPLv3',
	url = 'https://github.com/aanunez/TMed',
	packages = ['TMed'],
    entry_points={
        'console_scripts': [
            'tmed = tmed.__main__:main'
        ]
    },
)
