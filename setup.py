"""Setup configuration for the data science project."""

from setuptools import find_packages, setup

setup(
    name="tenacious-ds",
    version="0.1.0",
    description="A comprehensive data science project",
    author="kemboibilly408-cell",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "xgboost",
        "matplotlib",
        "seaborn",
        "plotly",
    ],
)
