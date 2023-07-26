from setuptools import setup, find_packages

setup(
    name='ezui',
    version='0.0.0',
    package=find_packages(),
    requires=[
        "colorama",
        "keyboard"
    ],
    author='Plunder283',
    author_email='plunder283@protonmail.com',
    description='A python module for easily creating a powerful and dynamic user interface in shell',
    url='https://github.com/Plunder283/ezui',
)