from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="tfcv",
    version="0.0.1",
    description="Various Deep Learning Models (tensorflow)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Shivam-21-11/Tf-Model-Packages",
    author="Shivam Singh",
    author_email="Shivamsingh2111@gmail.com",
    keywords=["Machine Learning","Computer Vision", "Generative adversarial networks","Deep Learning"],
    license="MIT",
    packages=["GAN", "Helper"],
    install_requires=['tensorflow','numpy','keras','matplotlib'],
    include_package_data=True,
)