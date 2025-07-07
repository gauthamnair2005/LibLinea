from setuptools import setup

setup(
    name="liblinea",
    version="2.2.0",
    py_modules=["liblinea","liblinea_weblet","liblinea_math","liblinea_network","liblinea_ai","liblinea_data"],
    description="The Core Module(s) for Linea Programming Language",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Gautham Nair",
    author_email="gautham.nair.2005@gmail.com",
    url="https://github.com/gauthamnair2005/LibLinea",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)