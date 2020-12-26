# Builds and installs ctfpwn
install:
		python3 setup.py sdist bdist_wheel
		python3 -m pip install -e .

