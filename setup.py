from setuptools import setup, find_packages
import os

# Build and publish to PyPI:
#   python setup.py sdist bdist_wheel
#   python -m twine check dist/*
#   python -m twine upload -r testpypi dist/*
#   python -m twine upload -r pypi dist/*

try:
    PROJECT_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(PROJECT_ROOT_DIR, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = """
# slash-fixer

Fixes slashes in your paths. Because Windows just had to be different.

See `README.md` for usage.

"""
setup(
    name='slash-fixer',
    description='Fixes slashes in your paths. Because Windows just had to be different.',
    version='2022.02.19',
    url='https://github.com/scholer/slash-fixer',  # project home page
    project_urls={  # Additional, arbitrary URLs
        "Bug Tracker": "https://github.com/scholer/slash-fixer/issues",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://github.com/scholer/slash-fixer",
    },
    download_url='https://github.com/scholer/slash-fixer/archive/master.zip',  # Update for each new version
    license='MIT License',
    author='Rasmus Scholer Sorensen',
    author_email='rasmusscholer@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # setuptools.find_packages() is generally preferred over manual listing.
    # packages=find_packages(exclude=['bin', 'docs', 'tests', 'examples']),
    py_modules=["slash_fixer"],
    # Use MANIFEST.in to specify which non-package files to include in the distribution
    # package_data={'git_status_checker': ['data/*.txt']}  # Data to include for each package.
    # include_package_data=True,  # ONLY for data under revision control? Or maybe also MANIFEST.in?
    entry_points={
        'console_scripts': [
            # console_scripts should all be lower-case, else you may get an error when uninstalling:
            'slash-fixer=slash_fixer:fix_slashes_cli',
            'fix-slashes=slash_fixer:fix_slashes_cli',
        ],
        # 'gui_scripts': []
    },
    install_requires=[],  # No dependencies.
    keywords=[
        "path", "separator", "slash", "slashes", "backslash", "backslashes",
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
    ],
)
