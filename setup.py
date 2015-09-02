from setuptools import setup

setup(
    name='python-nebrios-authentication',
    version='0.1.0',
    description="python-nebrios is a simple and easy-to-use package to make authenticated nebrios api requests from a python application.",
    packages=['nebrios_auth'],
    url='http://github.com/briem-bixly/python-nebrios-authentication/',
    author='briem-bixly',
    install_requires=[
        '-e git://github.com/briem-bixly/python-nebrios#egg=python-nebrios'
    ]
)