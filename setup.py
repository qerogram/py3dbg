import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="py3dbg", 
    version="1.0.0",
    author="Qerogram",
    author_email="qerogram@google.com",
    description="modified the PyDbg library to support x64 processes, enhancing its capabilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qerogram/py3dbg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)