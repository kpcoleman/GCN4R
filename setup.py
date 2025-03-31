from setuptools import setup
from setuptools.command.install import install
import subprocess
import os

PACKAGES=['pysnooper',
            'fire',
            'numpy',
            'pandas',
            'networkx',
            'torch',
            'scikit-learn',
            'scipy',
            # 'torch-scatter==2.0.4',
            # 'torch-cluster==1.5.4',
            # 'torch-sparse==0.6.1',
            # 'torch-geometric==1.5.0',
            # 'torch_spline_conv==1.2.0',
            'torchvision',
            'matplotlib',
            'seaborn',
            'plotly',
            'rpy2',
            'cdlib',
            'captum']

with open('README.md','r', encoding='utf-8') as f:
      long_description = f.read()

setup(name='gcn4r',
      version='0.1',
      description='Code to accompany GCN4R package.',
      url='https://github.com/jlevy44/GCN4R',
      author='Joshua Levy',
      author_email='joshualevy44@berkeley.edu',
      license='MIT',
      scripts=['bin/install_gcn4r_dependencies'],
      entry_points={
            'console_scripts':['gcn4r=gcn4r.cli:main']
      },
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['gcn4r'],
      install_requires=PACKAGES,
      package_data={'gcn4r': ['data/*']})
