from setuptools import find_packages
from distutils.core import setup

from pretty_times import VERSION


REQUIREMENTS = []

TEST_REQUIREMENTS = [
    'coverage',
    'pep8',
    'pyflakes',
    'nose',
    'nosexcover',
]


def do_setup():
    setup(
        name="pretty-times",
        version=VERSION,
        author="nixon",
        description="pretty_times provides fixes for the py-pretty library.",
        long_description=open('README.txt', 'r').read(),
        url="https://github.com/nixon/pretty-times",
        packages=find_packages(exclude=['example']),
        install_requires=REQUIREMENTS,
        tests_require=TEST_REQUIREMENTS,
        zip_safe=False,
    )


if __name__ == '__main__':
    do_setup()
