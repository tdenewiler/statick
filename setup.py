"""Setup."""


from setuptools import setup  # NOLINT

import statick_tool

with open("README.md", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()

TEST_DEPS = [
    "backports.tempfile",
    "pylint-django<2.0",
    "pytest",
    "mock",
    "tox",
]

EXTRAS = {
    "test": TEST_DEPS,
}

setup(
    name="statick",
    description="Making code quality easier.",
    author="SSC Pacific",
    version=statick_tool.__version__,
    packages=["statick_tool"],
    package_data={
        "statick_tool": [
            "rsc/.*",
            "rsc/*",
            "rsc/plugin_mapping/*",
            "plugins/*.py",
            "plugins/discovery/*",
            "plugins/tool/*",
            "plugins/reporting/*",
        ]
    },
    scripts=["statick"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    # Need to duplicate tests_require here due to a bug in pip-compile.
    # https://web.git.mil/mm/ci/-/jobs/199059
    install_requires=[
        "PyYAML",
        "backports.tempfile",
        "bandit",
        "black",
        "cmakelint",
        "cpplint",
        "deprecated",
        "docformatter",
        "flawfinder",
        "isort",
        "lizard",
        "mock",
        "mypy",
        "pycodestyle",
        "pydocstyle",
        "pyflakes",
        "pylint",
        "pylint-django<2.0",
        "pytest",
        "ruff",
        "tabulate",
        "tox",
        "xmltodict",
        "yamllint",
        "yapsy",
    ],
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
    url="https://github.com/sscpac/statick",
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
    ],
)
