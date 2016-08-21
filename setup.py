#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import kHole

setup(name='buttshock',
      version="{}".format(kHole.VERSION),
	  description='Python Libraries for controlling and reading the Minna kGoal Bluetooth Kegelcizer',
      long_description=(open('README.rst').read() + '\n' + open(os.path.join('CHANGES.rst')).read()),
      author='qDot',
      author_email='kyle@machul.is',
      url='http://github.com/metafetish/khole-py',
      license='BSD License',
      packages=find_packages(),
      keywords=['health', 'kegel', 'bluetooth'],
      install_requires=['pybluez', 'gattlib'],
      tests_require=['pytest'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: System :: Hardware :: Hardware Drivers'
      ]
)
