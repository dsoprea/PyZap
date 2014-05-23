from setuptools import setup, find_packages

def _pre_install():
      print("Verifying that the library is accessible.")

      import sys
      import os.path
      dev_path = os.path.dirname(__file__)
      sys.path.insert(0, dev_path)

      try:
            import pyzap.library
      except OSError as e:
            print("Library can not be loaded: %s" % (str(e)))
            raise


class _custom_install(install):
    def run(self):
        _pre_install()
        install.run(self)

description = "Python wrapper library for ZapLib digital television (DVB) " \
              "tuning library."

long_description = """\
This library allows a Python script to tune channels with nothing more than the 
ZapLib library, and the correct tuning values for the type of DVB that you're
trying to decode. No channels.conf file is required.
"""

setup(name='pyzap',
      version='0.3.1',
      description=description,
      long_description=long_description,
      classifiers=[
'Development Status :: 2 - Pre-Alpha',
'Topic :: Software Development :: Libraries :: Python Modules',
'Programming Language :: Python',
'Topic :: Multimedia :: Video :: Capture',
      ],
      keywords='dvb dvb-a dvb-c dvb-s dvb-t dvb-apps television cable',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/PyZap',
      license='GPL 2',
      packages=find_packages(exclude=[]),
      include_package_data=True,
      zip_safe=True,
      cmdclass={ 'install': _custom_install },
)
