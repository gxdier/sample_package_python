from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python_package_sample',
    version='0.1.0',
    decription='A sample python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gaetan Disdier',
    author_email='gaetan.disdier@gmail.com',
    classifier=['Development Status :: 3 - Alpha',
                'Intended Audience :: Myself',
                'Topic :: Software Development :: Build Tools',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                ],
    keyword='sample setuptools development',
    packages=find_packages(),
)
