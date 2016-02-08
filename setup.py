import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 2, 0):
    raise RuntimeError("uulm-mensa requires Python 3.2.0+")

setup(
    name='uulm-mensa',
    version='0.1.0',

    url='https://github.com/mmk2410/uulm-mensa',

    author='mmk2410',
    author_email='marcelmichaelkapfer@yahoo.co.nz',

    packages=find_packages(),

    platforms='any',

    description='Mensa plans for the university ulm',
    long_description=open('./README.md', 'r').read(),

    keywords='mensa plan bistro uulm ulm',

    install_requires=['datetime'],

    license='MIT',

    entry_points={
        'console_scripts': [
            'uulm-mensa=uulm_mensa.cli:main'
        ],
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
