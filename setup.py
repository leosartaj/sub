import os
from setuptools import setup

setup(
    name = 'sub',
    version = '0.0.3',
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Simple Tool to download Subtitles.'),
    license = 'MIT',
    keywords = 'subtitles download movies tv shows',
    url = 'http://github.com/leosartaj/sub',
    packages=['sub'],
    scripts=['bin/sub'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
