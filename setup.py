import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="test-package",
    version="0.0.1",
    author="Chen Weilin",
    author_email="2735378542@qq.com",
    packages=["bb"],
    description="write for bb",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)