# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages


VERSION_SUFFIX = "%d.%d" % sys.version_info[:2]


with open("README.rst") as readme:
    long_description = readme.read()


setup(
    name="pegasafe",
    version="1.0",
    description="Message summarization.",
    long_description=long_description,
    author="Sarthak Navjivan",
    install_requires=[
        "docopt>=0.6.1,<0.7",
        "breadability>=0.1.20",
        "requests>=2.7.0",
        "pycountry>=18.2.23",
        "nltk>=3.0.2,<3.2.0" if VERSION_SUFFIX == "3.3" else "nltk>=3.0.2",
    ],
    tests_require=[
        "pytest>=3.0.0",
        "pytest-cov",
        "pytest-watch",
    ],
    extras_require={
        "LSA": ["numpy"],
        "LexRank": ["numpy"],
        "Japanese": ["tinysegmenter"],
        "Chinese": ["jieba"],
    },
    packages=find_packages(),
    package_data={"pegasafe": [
        "data/stopwords/*.txt",
    ]},
    entry_points={
        "console_scripts": [
            "pegasafe = pegasafe.__main__:main",
            "pegasafe-%s = pegasafe.__main__:main" % VERSION_SUFFIX,
            "pegasafe_eval = pegasafe.evaluation.__main__:main",
            "pegasafe_eval-%s = pegasafe.evaluation.__main__:main" % VERSION_SUFFIX,
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",

        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Czech",
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: German",
        "Natural Language :: Japanese",
        "Natural Language :: Portuguese",
        "Natural Language :: Slovak",
        "Natural Language :: Spanish",

        "Topic :: Education",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Markup :: HTML",

        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
