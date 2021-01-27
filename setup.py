import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="albiapi",
    version="1.0.0",
    author="nolemretaW",
    author_email="watermelonpl@outlook.com",
    description="Open-source API for Polish site, Albicla",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nolemretaWxd/AlbiAPI",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
          'requests_toolbox'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)