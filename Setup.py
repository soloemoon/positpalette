"""Install positpalette

This script copies matplotlib styles. Based on the following stackoverflow answer:
https://stackoverflow.com/questions/31559225/how-to-ship-or-distribute-a-matplotlib-stylesheet and SciencePlots package by garrettj403

"""

from setuptools import setup
from setuptools.command.install import install
import os
import shutil
import atexit
import matplotlib
import glob

def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))
            
class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)
        
setup(
    name='positpalette',
    version='1.0.0',
    author="Solomon Moon",
    author_email="soloemoon@gmail.com",
    description="posit palettes,
    long_description="Generate Matplotlib, Seaboarn and Plotnine plots with Posit styling",
    long_description_content_type='text/markdown',
    license="MIT",
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "thesis-template",
        "matplotlib-styles",
        "python",
        "posit"
    ],
    url="https://github.com/soloemoon/positpalettes/",
    install_requires=['matplotlib', ],
    cmdclass={'install': PostInstallMoveFile, },
)
