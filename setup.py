import setuptools

setuptools.setup(
    name="AlbiAPI",
    version="1.0.0",
    author="nolemretaW",
    author_email="watermelonpl@outlook.com",
    description="Open-source API for Polish site, Albicla",
    long_description_content_type="text/markdown",
    url="https://github.com/nolemretaWxd/AlbiAPI",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
          'requests-toolbelt'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)