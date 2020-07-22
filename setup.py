import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name='python-pensionpro',
    version='0.2',
    license='MIT',
    author="Aaron Harabedian",
    author_email="aaronharabedian@gmail.com",
    description="Python library for interacting with PensionPro API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    python_requires='>=3.6',
)