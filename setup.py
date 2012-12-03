from setuptools import setup, find_packages
import sys, os

# TODO: Require zaplib library.

version = '0.1'

setup(name='pyzap',
      version=version,
      description="Python wrapper library for ZapLib digital television (DVB) tuning library.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='dvb dvb-a dvb-c dvb-s dvb-t dvb-apps television cable',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/PyZap',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
