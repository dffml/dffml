import os
import sys
import ast
import site
from io import open

from setuptools import find_packages, setup

# See https://github.com/pypa/pip/issues/7953
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

self_path = os.path.dirname(os.path.realpath(__file__))

with open(
    os.path.join(self_path, "dffml_feature_auth", "version.py"), "r"
) as f:
    for line in f:
        if line.startswith("VERSION"):
            version = ast.literal_eval(line.strip().split("=")[-1].strip())
            break

with open(os.path.join(self_path, "README.md"), "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="dffml_feature_auth",
    version=version,
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="John Andersen",
    author_email="john.s.andersen@intel.com",
    url="https://github.com/dffml/dffml/blob/main/feature/auth/README.md",
    license="MIT",
    keywords=[""],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    tests_require=[],
    packages=find_packages(),
    entry_points={
        "dffml.operation": [
            "scrypt = dffml_feature_auth.feature.operations:Scrypt"
        ]
    },
)
