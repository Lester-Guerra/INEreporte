from setuptools import setup, find_packages

setup(
    name='reporteine',
    version='0.1.2',
    author='Luis Alfredo Alvarado Rodríguez',
    description='Creador de reportes estilo INE.',
    long_description='',
    url='https://github.com/1u1s4/INE_LaTeX',
    keywords='development, setup, setuptools',
    python_requires='>=3.9',
    packages=find_packages(),
    py_modules=['funcionesINE', 'funcionesjo', 'reporteine', 'WS_orga_INE', 'xlsxchef'],
    install_requires=[
        'geopandas',
        'matplotlib',
        'beautifulsoup4==4.11.1',
        'bs4==0.0.1',
        'certifi==2022.9.24',
        'cffi==1.15.1',
        'charset-normalizer==2.1.1',
        'et-xmlfile==1.1.0',
        'fredapi==0.5.0',
        'idna==3.4',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.1',
        'numpy==1.23.4',
        'openpyxl==3.0.10',
        'packaging==21.3',
        'pandas==1.5.1',
        'pycparser==2.21',
        'pyodbc==4.0.34',
        'pyparsing==3.0.9',
        'python-dateutil==2.8.2',
        'pytz==2022.6',
        'pytz-deprecation-shim==0.1.0.post0',
        'requests==2.28.1',
        'rpy2==3.5.5',
        'six==1.16.0',
        'soupsieve==2.3.2.post1',
        'tzdata==2022.6',
        'tzlocal==4.2',
        'urllib3==1.26.12',
        'xlrd==2.0.1',
        'XlsxWriter==3.0.3'
    ],
    package_data={
        'reporteine': ['Fuentes/*', 'Plantilla/*', 'plantillas_direcciones/*'],
    },
    include_package_data=True,
)
