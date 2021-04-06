# python-sinamics
Python codes to work with [Siemens SINAMICS inverters](https://new.siemens.com/global/en/products/drives/sinamics.html) via [Snap7 library](http://snap7.sourceforge.net/).

## Description
This project contains a class definition for control/monitoring of SINAMICS inverters via TCP/IP using application layer [S7 protocol](https://wiki.wireshark.org/S7comm). For this, it utilizes the [python-snap7 library](https://python-snap7.readthedocs.io).

The [python-snap7 library](https://python-snap7.readthedocs.io) has a python wrapper for S7 communication/read/write functions of [Snap7 library](http://snap7.sourceforge.net/).

The codes in [Main](Main/) folder are:
- [sinamics.py](Main/sinamics.py) : Class definition to read/write parameters of SINAMICS inverters.
- [sinamics_graph.py](Main/sinamics_graph.py) : A function definition built upon the class Sinamics to obtain traces from the inverter.

## How to use
This code should be executed as a module (using import), placing the desired [Main](Main/) folder files in your program folder or a common python folder such as ../site-packages/

As [documentation defines](https://python-snap7.readthedocs.io/en/latest/introduction.html), python-snap7 library was built for python 2.7, however the codes written here (sinamics.py and sinamics_graph.py) were tested with several versions of python without any issue (python 2.7, python 3.5.3, python 3.6, python 3.7).

The required dependencies to run the codes:
- sinamics.py : python-snap7 and snap7 build
- sinamics_graph.py : python-snap7 and snap7 build, matplotlib.

## Installation of snap7
For installation of snap7 build, see:
- [Snap7 Source](http://snap7.sourceforge.net/home.html)

Basically:
1. Download the .7z file: https://sourceforge.net/projects/snap7/files/1.4.2
2. Extract the content and then:
    - For Windows OS:
        - Place the dll 'build/bin/win<32|64>/snap7.dll' inside any directory that is contained in the PATH variable.
    - For Linux OS:
        - After extracting the zipped file (maybe 'sudo' before 3rd or 4th command depending on user rights):
            ```
            cd build/unix
            make -f "$(uname -m)_linux.mk"
            cp "../bin/$(uname -m)-linux/libsnap7.so" /usr/lib
            ldconfig
            ```

## Installation of python-snap7 library
For complete information on the installation:
- [Python-snap7 Installation procedure](https://python-snap7.readthedocs.io/en/latest/installation.html)

Basically:
```
    pip install python-snap7
```

## Documentation
Complete information regarding snap7 and python-snap7 can be seen in the docs bellow:
- [Python-snap7 Read the Docs](https://python-snap7.readthedocs.io)
- [Python-snap7 Github](https://github.com/gijzelaerr/python-snap7)
- [Snap7 Source](http://snap7.sourceforge.net/home.html)

More information regarding the S7 protocol can be seen in:
- [Gmiru Article-part1](http://gmiru.com/article/s7comm/)
- [Gmiru Article-part2](http://gmiru.com/article/s7comm-part2/)
