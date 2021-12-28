from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python package to be used with Matrix SIM Switch Box tool'
LONG_DESCRIPTION = 'This package was created to be used with Matrix SIM Switch Box,'\
    'a tool provided by Qualigon to manipulate sim cards in mobile devices.'\
    'More informations can be found at https://www.qualigon.de/en/test-systems/matrix-sim-switchbox-mssb'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="mssb", 
        version=VERSION,
        author="Antonio Carlos",
        author_email="antoniocarlos048@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'mssb'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
