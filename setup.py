from setuptools import setup

setup(
    name='Dashgourd-Web-Api-Client',
    version='0.1',
    url='https://github.com/richard-to/dashgourd-web-api-client',
    author='Richard To',
    description='Example web api client for Dashgourd',
    platforms='any',
    packages=[
        'dashgourd'
    ],
    namespace_packages=['dashgourd'],    
    include_package_data=True,
    install_requires=[
        'Requests'
    ]    
)
