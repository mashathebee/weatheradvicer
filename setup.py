from setuptools import setup, find_packages
setup(
    name="weatheradvicer",
    version="0.0.1",
    packages=find_packages("."),
    entry_points = {
        "console_scripts": [
            "weather=weatheradvicer.cli:main"
        ]
    },
    setup_requires = [
        "pytest-runner"
    ],
    tests_require = [
        "pytest"
    ],
)
