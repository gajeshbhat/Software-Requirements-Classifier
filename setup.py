from setuptools import setup, find_packages

setup(
    name="requirements-classifier",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "fpdf",
        "PyPDF2"
    ],
    entry_points={
    "console_scripts": [
        "reqclass=app.cli:main" 
    ]
    }
    ,
    author="Gajesh Bhat",
    description="A CLI tool to classify software requirements using LLMs (via Ollama)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
