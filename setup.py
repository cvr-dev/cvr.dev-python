import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cvr",
    description="Official Python client for https://cvr.dev",
    version="0.2.1",
    author="cvr.dev",
    author_email="kontakt@cvr.dev",
    packages=["cvr", "cvr.dto"],
    options={'bdist_wheel': {'universal': True}},
    python_requires='>=3.5',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cvr-dev/cvr.dev-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development",
    ],
)
