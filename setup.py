import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ctfpwn",
    version="1.0.0",
    description="Framework for making CTFs, bug bounty and pentesting Python scripting easier",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bl4de/ctfpwn",
    author="Rafal Janicki @bl4de",
    author_email="bloorq@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
    packages=["ctfpwn"],
    include_package_data=True,
    install_requires=["requests", "hashlib", "base64"],
    entry_points={
        "console_scripts": [
            "ctfpwn=ctfpwn.__main__:main",
        ]
    },
)
