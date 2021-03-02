from setuptools import setup

v_temp = {}
with open("pedigree_matrix/version.py") as fp:
    exec(fp.read(), v_temp)
version = ".".join((str(x) for x in v_temp["version"]))


setup(
    name="pedigree_matrix",
    version=version,
    packages=["pedigree_matrix"],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license="BSD 3-clause",
    install_requires=[],
    url="https://github.com/brightway-lca/pedigree_matrix",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    description="A python implementation of the Ecoinvent pedigree matrix for estimating uncertainty data for life cycle inventories",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
