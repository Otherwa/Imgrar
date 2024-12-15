from setuptools import setup, find_packages

setup(
    name="Imgrar",  # Package name
    version="1.0.1",  # Version
    packages=find_packages(where="src"),  # Automatically finds packages inside 'src'
    package_dir={"": "src"},  # Tells setuptools to look for packages under 'src'
    author="Atharv Desai",
    author_email="atharvdesai2002@gmail.com",
    description="Small code files to Images and Vice-Versa",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Otherwa/Imgrar",
    install_requires=[
        "Pillow",  # List any dependencies you need
    ],
    entry_points={
        "console_scripts": [
            "imgrar-cli=ImgRar.cli:main",  # The CLI entry point (change `cli.py` to the right module)
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
