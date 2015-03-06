"""
mfa
===

Multi-factor authentication on your command line.

"""
from setuptools import setup


setup(
    name='mfa',
    version='0.1.1',
    url='https://github.com/limeburst/mfa',
    author='Jihyeok Seo',
    author_email='me@limeburst.net',
    description='Multi-factor authentication on your command line',
    long_description=__doc__,
    packages=['mfa'],
    entry_points={
        'console_scripts': ['mfa = mfa.cli:cli']
    },
    install_requires=[
        'click',
        'keyring',
        'onetimepass'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities'
    ]
)
