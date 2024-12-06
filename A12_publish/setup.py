from setuptools import setup, find_packages

setup(
    name="crime_test",
    version="1.0.0",
    author="Aaron D'Souza",
    author_email="aaron.dsouza@sjsu.edu",
    description="A library for crime data validation and statistical calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy==2.1.3",
        "pandas==2.2.3",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.2",
        "six==1.17.0",
        "tzdata==2024.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

