**Description of files in this folder**

Tagmukay-Bold.vfb - FontLab master file (has designer friendly postscript names)
Tagmukay-Regular.vfb - FontLab master file (has designer friendly postscript names)

FLSetPSNames_uniTAGMUKAY.py - FontLab macro to convert designer friendly names 
to Adobe Gyph List postscript names. *Has a dependency on PSNames_uni.py*. 
Run the macro in FontLab before generating the source TTF file. The code in 
OpenType "fea" files and Graphite "gdl" files is written using AGL names.

PSNames_uni.py - Python module. Install in your Python Library.

psnames.csv - a reference list of designer friendly names and AGL postscript names 
for Tagmukay
