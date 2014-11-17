try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def readFile(fName):
    with open(fName) as f:
        lines = f.read()
    return lines

setup(
    name = 'sub',
    version = '0.0.7',
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Simple Tool to download Subtitles.'),
    long_description = readFile('README.md'),
    license = 'MIT',
    keywords = 'subtitles download movies tv shows',
    url = 'http://github.com/leosartaj/sub',
    packages=['sub'],
    scripts=['bin/sub'],
    install_requires = ['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
