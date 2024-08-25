import os

from setuptools import setup

VERSION = "v0.0.0a0"


def get_long_description():
    with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
            encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="sysconfig_extra",
    description="python -m sysconfig_extra",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Florents Tselai",
    url="https://github.com/Florents-Tselai/sysconfig-extra",
    project_urls={
        "Issues": "https://github.com/Florents-Tselai/sysconfig-extra/issues",
        "CI": "https://github.com/Florents-Tselai/sysconfig-extra/actions",
        "Changelog": "https://github.com/Florents-Tselai/sysconfig-extra/releases",
    },
    license=open("LICENSE").read(),
    version=VERSION,
    packages=["sysconfig_extra"],
    install_requires=["pip", "setuptools"],
    extras_require={
        "test": [
            "pytest"
        ]
    },
    python_requires=">=3.7",
)
