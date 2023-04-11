import setuptools

setuptools.setup(
    include_package_data = True,
    name = 'calc2243336',
    version = '0.0.2',
    description = 'calc example for Pypi',
    author = 'SangKyunJeon',
    author_email = 'sangkyun.jeon@gmail.com',
    url = 'https://github.com/jsk0910/calc2243336',
    download_url = 'https://github.com/jsk0910/calc2243336/archive/refs/tags/v.0.0.2.zip',
    install_requires = ['pytest'],
    packages = ['mycalc'],
    long_description = 'oss-dev calculator example',
    long_description_content_type = 'text/markdown',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operatig System :: OS Independent"
    ]
)
