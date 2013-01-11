from setuptools import setup, find_packages
import sys, os

# TODO: Require zaplib library.

version = '0.2.2'

setup(name='pyzap',
      version=version,
      description="Python wrapper library for ZapLib digital television (DVB) tuning library.",
      long_description="""\
This library allows a Python script to tune channels with nothing more than the 
ZapLib library, and the correct tuning values for the type of DVB that you're
trying to decode. No channels.conf file is required.
""",
      classifiers=[
'Development Status :: 2 - Pre-Alpha',
'Topic :: Software Development :: Libraries :: Python Modules',
# TODO: Check if this should be version 2 or 3.
'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
'Programming Language :: Python',
'Topic :: Multimedia :: Video :: Capture',
],
      keywords='dvb dvb-a dvb-c dvb-s dvb-t dvb-apps television cable',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/PyZap',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
