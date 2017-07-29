try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup#from distutils.core import setup
from setuptools import setup

setup(
    name='RFID-UUID-USB-Card-Reader',
    version='0.1.0',
    author='Peter Steensen',
    author_email='peter.steensen.fl@googlemail.com',
    packages=['uuidreader', 'uuidreader.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/RFID-UUID-USB-Card-Reader/',
    license='LICENSE.txt',
    description='RFID to UUID script for USB Card Reader',
    long_description=open('README.txt').read(),
    install_requires=[
        "evdev  == 0.7.0",
        "uuid == 1.30",
    ],
)
