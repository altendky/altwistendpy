import setuptools

import versioneer


setuptools.setup(
    name='altwistendpy',
    description="Extras for working with Twisted.",
    author='Kyle Altendorf',
    author_email='sda@fstab.net',
    url='https://github.com/altendky/altwistendpy',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'amp = altwistendpy.examples.amp.cli:cli',
        ],
    },
    install_requires=[
        'attrs',
        'click',
        'twisted',
    ],
    extras_require={
        'dev': [
            'gitignoreio',
        ],
    },
)
