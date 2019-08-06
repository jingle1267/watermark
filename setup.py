# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-08-05 17:30
@desc：  : 
"""

from distutils.core import setup

from setuptools import find_packages

setup(
	name='watermark2',
	version='1.0.3',
	description=(
		'给图片添加文字水印，支持设置文字内容、大小、透明度、颜色、旋转等'
	),
	long_description=open('README.rst').read(),
	author='jingle1267',
	author_email='jingle1267@163.com',
	maintainer='jingle1267',
	maintainer_email='jingle1267@163.com',
	license='MIT',
	packages=find_packages(),
	platforms=["all"],
	url='https://github.com/jingle1267/watermark.git',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	keywords='watermark'
)
