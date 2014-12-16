try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from sub import __version__ # version number

def readFile(fName):
    with open(fName) as f:
        lines = f.read()
    return lines

setup(
    name = 'sub',
    version = __version__,
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Simple Tool to download Subtitles.'),
    long_description = open('README.rst').read(),
    license = 'MIT',
    keywords = 'subtitles download movies tv shows',
    url = 'http://github.com/leosartaj/sub',
    packages=find_packages(),
    scripts=['bin/sub'],
    install_requires = ['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
