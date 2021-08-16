from setuptools import setup

setup(
    name='esdao',
    version='0.1.0',
    description='Thin abstraction layer for Elasticsearch',
    url='https://github.com/OneTesseractInMultiverse/esdao',
    author='Pedro Guzmán',
    author_email='info@subvertic.com',
    license='MIT',
    packages=['esdao'],
    install_requires=[
        'elasticsearch',
        'jsonplus',
        'pydantic'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
    ],
)
