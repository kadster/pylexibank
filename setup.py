from setuptools import setup, find_packages


setup(
    name='pylexibank',
    version='2.8.3.dev0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='Python library implementing the lexibank workbench',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='',
    license='Apache 2.0',
    url='https://github.com/lexibank/pylexibank',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.commands': [
            'lexibank=pylexibank.commands',
        ],
        'cldfbench.scaffold': [
            'lexibank_simple=pylexibank.scaffold:LexibankTemplate',
            'lexibank_combined=pylexibank.scaffold:LexibankCombinedTemplate',
        ],
    },
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'attrs>=19.2',
        'segments>=2.1.1',
        'cldfbench[excel]>=1.0',
        'csvw>=1.5.6',
        'clldutils>=2.8.0',
        'pycldf>=1.15.2',
        'pyglottolog>=2.0',
        'pyconcepticon>=2.1.0',
        'pyclts>=2.0,<3.0',
        'lingpy>=2.6.5',
        'appdirs',
        'requests',
        'termcolor',
        'gitpython',
        'tqdm',
        'bs4',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'pytest>=5',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
