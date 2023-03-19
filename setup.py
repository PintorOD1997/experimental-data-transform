from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name='transform_module',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'mi_comando = mi_modulo.archivo1:funcion1',
            'otro_comando = mi_modulo.archivo2:funcion2'
        ]
    },
    author='Diego Pintor Ochoa, Daniela Michel Mercado, Ana María Aguilera Gómez',
    author_email='dpintor1997@gmail.com, etc..',
    description='Transformación y escritura de archivos para el SIG',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://url-del-repositorio',
    project_urls={
        'Código fuente': 'https://url-del-repositorio',
        'Reporte de problemas': 'https://url-del-repositorio/issues',
    },
)

