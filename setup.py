from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="myvectors",
    packages=["myvectors"],
    version="0.1",
    description=" Exploring VECTOR Mathematics ",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SHREYAS1188/vector_python_package",
    download_url = "https://github.com/SHREYAS1188/vector_python_package/archive/0.1.tar.gz",
    author="Shreyas Potdar",
    author_email="shreyasmp2001@gmail.com",
    license="MIT",
    include_package_data=True,
    install_requires=["math"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.8",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7",
    ],
)
