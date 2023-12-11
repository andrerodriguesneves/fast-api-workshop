import io
import os
from setuptools import setup, find_packages


def read(*paths, **kwargs):
    """Read file and return content."""
    with io.open(
        os.path.join(*paths), 
        encoding=kwargs.get("encoding", "utf8")
    ) as open_file:
        content = open_file.read().strip()    
    return content


def read_requirements(path):
    return[
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="pamps",
    version="0.1.0",
    description="",
    url="pamps.io",
    python_requires=">=3.8",
    long_description="Pamps is a social posting app",
    long_description_content_type="text/markdown",
    author="PAMPS",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["pamps = pamps.app:main"]
    }

)