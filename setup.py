from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cnv',
    version='0.1',
    author="Eduardo de Santana Medeiros Alexandre",
    author_email="eduardo.ufpb@gmail.com",
    description="Um pequeno script para auxiliar na utilização da comunicação não violenta",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edusantana/cnv",
    #packages=setuptools.find_packages(),
    py_modules=['cnv'],
    install_requires=[
        'Click','click_didyoumean', 'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        cnv=cnv:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
#    python_requires='>=3.4',
)
