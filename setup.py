"""Setup file for commonlib."""

import pathlib
import setuptools


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="commonlib",
    version="0.0.1",
    description="An simple Python package",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/shunsvineyard/commonlib",
    author="Shun Huang",
    author_email="shunsvineyard@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7"
)
