from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'GUI for MG-PSO'
LONG_DESCRIPTION = 'GUI for MG-PSO'

# Setting up
setup(
    name="mg-pso-gui",
    version=VERSION,
    author="Robert Cordingly",
    author_email="<rcording@uw.ed>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 
                      'numpy', 
                      'requests',
                      'tkinter',
                      'customtkinter',
                      'plotly'],
    keywords=['python', 'muti-group', 'pso', 'particle', 'swarm', 'optimization', 'gui'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)