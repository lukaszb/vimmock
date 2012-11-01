import os
import sys
from setuptools import setup, find_packages

vimmock = __import__('vimmock')
readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
try:
    long_description = open(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(
    name = 'vimmock',
    version = vimmock.get_version(),
    url = 'http://github.com/lukaszb/vimmock',
    author = 'Lukasz Balcerzak',
    author_email = 'lukaszbalcerzak@gmail.com',
    download_url = 'http://github.com/lukaszb/vimmock/downloads',
    description = vimmock.__doc__.strip(),
    long_description = long_description,
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    scripts = [],
    requires = [],
    license = 'BSD',
    tests_require = [
        'mock',
        'unittest2',
    ],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Plugins',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Testing',
                   'Topic :: Text Editors',
    ],
    test_suite = 'vimmock.tests',
)

