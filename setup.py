from setuptools import setup

setup(
    name='DashGourd-Web-Api-Client',
    version='0.1',
    url='https://github.com/richard-to/dashgourd-web-api-client',
    author='Richard To',
    description='Example web api client for DashGourd',
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
