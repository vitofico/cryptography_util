from setuptools import setup

setup(name='cryptography_util',
      version='0.2',
      description='Small utility script for encrypt/decrypt files using Fernet algorithm.',
      url='https://github.com/vitofico/cryptography_util',
      author='Vito Mario Fico',
      author_email='undisclosed@gmail.com',
      license='GNUv3',
      packages=['cryptography_util'],
      install_requires=['cryptography',],
      scripts=['bin/crypto-util.py'],
      zip_safe=False)