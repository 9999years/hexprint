from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='hexprint',
    version='0.0.1',

    description='''A utility for printing raw bytes to the console or converting a string like `1b 20 f9` or `1B20F9` into the bytes b'\x1b\x20\xf9'.''',
    long_description='https://github.com/9999years/hexprint',
    url='https://github.com/9999years/hexprint',
    author='Rebecca Turner',
    author_email='637275@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
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
