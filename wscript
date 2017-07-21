#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file

# set the default output folders
out="results"
DOCDIR=["documentation", "web"]
OUTDIR="installers"
ZIPDIR="releases"
TESTDIR='tests'
TESTRESULTSDIR='tests'
STANDARDS='tests/standards'

# set the font name, version, licensing and description
APPNAME='Tagmukay'
VERSION='2.000'
TTF_VERSION=VERSION
COPYRIGHT='Copyright (c) 2006-2017 SIL International'
LICENSE='OFL.txt'
DESC_SHORT='Tifinagh Unicode TrueType font with OT and Graphite support'

DESC_LONG='''
Tagmukay is a Shifinagh (also know as Tifinagh) script font with support for the 
Tawallammat Tamajaq language. It is a Unicode font that features bi-consonant 
ligatures and alternate forms necessary to support this language. It has Graphite 
and OpenType tables that have the logic to support these features.
'''

DEBPKG='fonts-sil-tagmukay'

# os/2 bits for the font since FontLab 5.2 doesn't provide the bit for Tifinagh
os2bits = "00000004000000000000200AA000007F"


for style in ('-Regular', '-Bold') :
    fontbase = 'Tagmukay' + style
    font (target = process(fontbase + '.ttf', name('Tagmukay'),
            cmd('hackos2 -q -u ' + os2bits + ' ${DEP} ${TGT}'),
            cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
        source = 'source/' + fontbase + '-source.ttf',
        version = TTF_VERSION,
        copyright = COPYRIGHT,
        license = ofl('Tagmukay', 'SIL'),
        opentype = fea ( 'source/' +  fontbase + '.fea', no_make = 1),
        graphite = gdl ( 'source/Tagmukay.gdl', no_make = 1),
        script = ['tfng'],
        pdf = fret(),
        woff = woff('web/Tagmukay' + style + '.woff', params = '-v ' + VERSION + ' -m ../source/Tagmukay-WOFF-metadata.xml'),
    )

def configure(ctx) :
    ctx.find_program('ttfautohint')
