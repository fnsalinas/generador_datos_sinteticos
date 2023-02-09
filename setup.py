
from setuptools import setup, find_packages

setup(
    name='Synthetic data generator',
    version='1.0',
    description='Program to generate synthetic data.',
    author='Fabio Salinas',
    author_email='fabio.salinas1982@gmail.com',
    license='',
    packages=find_packages(
        where='src',
        include=['src', 'src.*']
    ),
    package_dir={
        '':'src'
    },
    zip_safe=False
)
