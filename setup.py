from setuptools import setup
# install localy:
# python -m pip install -e ctfpwn

# This call to setup() does all the work
setup(
    name="ctfpwn",
    version="1.0.0",
    description="Framework for making CTFs, bug bounty and pentesting Python scripting easier",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/bl4de/ctfpwn",
    author="Rafal Janicki @bl4de",
    author_email="bloorq@gmail.com",
    license="MIT",
    packages=["ctfpwn"],
    install_requires=["requests"]
)
