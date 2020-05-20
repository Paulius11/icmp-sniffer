import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# This call to setup() does all the work
setup(
    name="icmp_sniffer",
    version="0.0.3",
    description="Scans ping packages and posts them to mongodb.",
    author="Paulius",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["icmp_sniffer"],
    include_package_data=True,
    # install_requires=["pymongo==3.10.1", "scapy==2.4.3"],
    entry_points={
        "console_scripts": [
            "icmpsn=icmp_sniffer.__main__:main",
        ]
    },
)