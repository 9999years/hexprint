from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# generate eskymap from dat
from eskytools import regen_map
regen_map.main()

setup(
    name='uni2esky',
    version='1.0.3',

    description='''Utilities for inspecting unknown code pages of printers or terminals and for interfacing with the Esky POS-58 printer specifically.''',
    # rst is some bull shit and i will not be party to it. markdown or die
    long_description='https://github.com/9999years/uni2esky/blob/master/readme.md',
    url='https://github.com/9999years/uni2esky',
    author='Rebecca Turner',
    author_email='637275@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Utilities',
        'Natural Language :: English',
    ],

    keywords='io lowlevel hex',

    packages=find_packages(exclude=['contrib', 'docs', 'tests',]),

    entry_points={
        'console_scripts': [
            'hexprint=hexprint.hexprint:main'
        ],
    },
)
