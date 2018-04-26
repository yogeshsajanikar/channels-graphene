from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies
    'channels >= 2.0.0'
]

setup(
    name='channels-graphene',
    version=version,
    description="'GraphQL support for channels consumers'",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers  # noqa: E501
    ],
    keywords='api graphql graphene django channels',
    author='Yogesh Sajanikar',
    author_email='yogesh_sajanikar@yahoo.com',
    url='',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['channels-graphene=channels.graphene:main']
    })
