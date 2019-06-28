import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tuyaha",
    version="0.0.1",
    author="Pavlo Annekov",
    author_email="paul.annekov@gmail.com",
    description="A Python library that implements a Tuya API endpoint that was specially designed for Home Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
)