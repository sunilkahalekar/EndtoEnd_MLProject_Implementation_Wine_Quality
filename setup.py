import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "EndtoEND_MLProject"
AUTHOR_USER_NAME= 'sunilkahalekar'
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "kahalekar.sunil@gmail.com"


setup(
    name=SRC_REPO
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A End to End ML project',
    long_description='EndtoEnd_MLProject_Implementation_Wine_Quality',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0,,
        'jupyter'
    ],
    package_data={
        'sample': ['sample_data.csv'],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)