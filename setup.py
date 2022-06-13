from setuptools import setup
from setuptools import find_packages

setup(
    name='petrocks',
    version='0.3.1',    
    description='Package for making pet rocks',
    url='https://github.com/srh-sloan/pet-rocks',
    author='Sarah Sloan',
    author_email='blah@example.com',
    license='MIT',
    package_dir={'':'src'},
    packages=find_packages('src'),
    install_requires=[],
)
