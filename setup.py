from setuptools import setup

setup(
    name='talan',
    version='0.1.1',    
    description='a Technical Algorithmic Analytics Python package',
    url='https://github.com/beyondbond/talan',
    author='Stephen Hudson',
    author_email='ted@beyondbond.com',
    license='BSD 2-clause',
    packages=['talan'],
    install_requires=['pandas','numpy'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Investment/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
)
