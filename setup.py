import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oduduwalang", 
    version="0.1.0",
    author="Oduduwa Developer",
    author_email="hello@oduduwalang.org",
    description="A Yoruba-first programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/OduduwaLang",
    project_urls={
        "Bug Tracker": "https://github.com/your-username/OduduwaLang/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "oduduwa=oduduwa.cli:main",
        ],
    },
)
