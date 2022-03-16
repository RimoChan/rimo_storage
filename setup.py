import setuptools


setuptools.setup(
    name='rimo_storage',
    version='1.3.1',
    author='RimoChan',
    author_email='the@librian.net',
    description='好！',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/rimo_storage',
    packages=['rimo_storage'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
