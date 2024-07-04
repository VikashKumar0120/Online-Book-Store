'''
Created on 23-July-2024

@author: Vikash Kumar 
'''
from setuptools import setup
setup(
    name='Online Book Store',
    version=1.0,
    url='https://github.com/siddhiparkar151992/Py_Shopping_Cart',
    author='Vikash Kumar',
    author_email='vikashkumar30526@gmail.com',
    description='A shopping cart',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    packages=['BookStore'],
    install_requires=[
        'virtualenv>=14.0.3',
        'Flask>=0.10.1',
        'flask-restful>=0.3.5',
        'pymysql>=0.7.1',
        'pymongo>=3.2.3',
        'jsonpickle>= 0.9.3'
    ]
      
)
