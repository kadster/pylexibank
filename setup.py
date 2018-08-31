from setuptools import setup, find_packages


setup(
    name='pylexibank',
    version='0.11.1.dev0',
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
        'console_scripts': [
            'lexibank=pylexibank.__main__:main',
        ],
    },
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'six',
        'attrs>=0.18.1',
        'pycldf>=1.5.1',
        'clldutils>=2.4.1',
        'pyglottolog',
        'pyconcepticon',
        'pyclts>=0.2',
        'segments>=2.0.1',
        'lingpy',
        'appdirs',
        'requests',
        'termcolor',
        'gitpython',
        'tqdm',
        'xlrd',
        'prompt_toolkit~=1.0',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'mock',
            'pytest>=3.1',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
