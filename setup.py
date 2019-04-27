from setuptools import setup

setup(
        name='sehavniva',
        version='1.0.1',
        packages=['sehavniva'],
        url='https://github.com/mflage/sehavniva-python',
        keywords = ['kartverket', 'sehavniva', 'iot', 'tide', 'sensor', 'smarthome', 'automation'],
        license='Apache 2.0',
        author='Marius Flage',
        author_email='mflage@gmail.com',
        description='Unofficial Python library for the SeHavNiva API',
        install_requires = ['requests', 'xmltodict'],
    )



