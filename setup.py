from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in stackinfo/__init__.py
from stackinfo import __version__ as version

setup(
	name="stackinfo",
	version=version,
	description="custom app",
	author="ujjwal",
	author_email="pathakujjwal93@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
