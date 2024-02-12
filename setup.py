from setuptools import setup, find_packages

setup(
    name='botality',
    version='0.1.0',
    author='botality',
    author_email='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/UBI-dev/botality',
    packages=find_packages(),
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GPL 3.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
