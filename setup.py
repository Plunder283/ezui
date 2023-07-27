from setuptools import setup, find_packages

VERSION = '0.0.0'
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='ezui',
    version=VERSION,
    requires=[
        "colorama",
        "keyboard"
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Plunder283',
    author_email='plunder283@protonmail.com',
    description='A powerful and user-friendly Python library for creating dynamic command-line user interfaces.',
    keywords=["ui", "user interface", "interface", "GUI"],
    url='https://github.com/Plunder283/ezui',
)