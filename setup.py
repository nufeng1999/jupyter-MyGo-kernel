#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyGo_kernel',
      version='0.0.1',
      description='Minimalistic Go kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyGo-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyGo-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyGo_kernel/install_MyGo_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'Go'],
      include_package_data=True
      )
