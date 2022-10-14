from setuptools import setup

setup(name='cryptography_util',
      version='0.1',
      description='Small utility script for encrypt/decrypt files using Fernet algorithm.',
      url='https://github.com/vitofico/cryptography_util',
      author='Vito Mario Fico',
      author_email='undisclosed@gmail.com',
      license='GNUv3',
      packages=['cryptography_util'],
      install_requires=['cryptography',],
      zip_safe=False)