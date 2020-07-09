import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="helicopter",
    version="0.0.5",
    description="Linking SciML Julia helicopter challenge to Microprediction.Org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/helicopter",
    author="microprediction",
    author_email="info@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["helicopter"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["numpy","pandas","pathlib","requests","microprediction>=0.9.11","copulas","matplotlib"],
    entry_points={
        "console_scripts": [
            "microprediction=microprediction.__main__:main",
        ]
     },
     )
