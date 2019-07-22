from setuptools import setup

setup(
    name = 'sehavniva-python',
    version = '0.1',
    packages = ['sehavniva-python'],
    url = 'https://github.com/mflage/sehavniva-python',
    download_url = "https://github.com/mflage/sehavniva-python/archive/v_01.tar.gz"
    keywords = ['kartverket', 'sehavniva', 'iot', 'tide', 'sensor', 'smarthome', 'automation'],
    license = 'MIT',
    author = 'Marius Flage',
    author_email = 'marius@flage.org',
    description = 'Unofficial Python library for the Norwegian Mapping Authority\'s SeHavNiva API',
    install_requires = ['requests', 'xmltodict'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
    )



