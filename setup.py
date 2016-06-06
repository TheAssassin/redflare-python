from setuptools import find_packages, setup

setup(
    name="redflare",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "tornado==4.3",
    ],
    package_data = {
        "": ["privilege-icons/*.svg"],
    }
)
