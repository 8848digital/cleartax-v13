from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cleartax_integration/__init__.py
from cleartax_integration import __version__ as version

setup(
	name="cleartax_integration",
	version=version,
	description="v-13 Compatibility for cleartax app",
	author="8848 Digital LLP",
	author_email="contact@8848digital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
