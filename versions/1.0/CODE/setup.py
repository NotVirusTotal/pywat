from setuptools import setup, find_packages

# Leer el archivo README.md como descripción larga
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pywat",  # Nombre de la librería
    version="1.0.0",  # Versión inicial
    author="TheWhiteCreator",  # Autor
    description="Python Windows Advanced Tools (PyWAT) - A comprehensive toolset for Windows system operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NotVirusTotal/pywat",  # URL del repositorio del proyecto
    packages=find_packages(),  # Detecta automáticamente todos los paquetes y subpaquetes
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",  # Licencia personalizada
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",  # Versión mínima de Python requerida
    install_requires=[
        "psutil>=5.8.0",  # Ejemplo de dependencia
        "pywin32>=300",  # Dependencia de PyWin32
    ],
    entry_points={
        "console_scripts": [
            "pywat-cli=pywat.cli:main",  # Ejemplo de comando CLI opcional si quieres incluir una herramienta de línea de comandos
        ],
    },
    include_package_data=True,  # Incluye otros archivos como el README.md y LICENSE
    zip_safe=False,  # Recomendación para evitar problemas con algunos archivos binarios
)
