from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="thatdslibrary",
    version="0.1.0",
    author="Quan Tran",
    author_email="anhquan0412@gmail.com",
    description="A useful package for EDA and quick ML model finetuning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anhquan0412/that_ds_library",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.23.0",
        "scikit-learn>=1.2.0",
        "matplotlib>=3.7.0",
        "pandas>=1.5.0",
        "plotly>=5.14.0",
        "dtreeviz>=2.2,
        "graphviz>=0.20",
        "seaborn>=0.12.0",
        "statsmodels>=0.13.0",
        "pingouin>=0.5.3",
    ],
)
