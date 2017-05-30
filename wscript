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
COPYRIGHT='Copyright (c) 2006-2017 SIL International, all rights reserved'
LICENSE='OFL.txt'	
DESC_SHORT='Tifinagh Unicode TrueType font with OT and Graphite support'

DEBPKG='fonts-sil-tagmukay'

# os/2 bits for the font since FontLab 5.2 doesn't provide the bit for Tifinagh
os2bits = "00000004000000000000200AA000007F"
# data file to change designer glyph names (in -source ttf) to Adobe glyph names which are used in fea and gdl
psnames = '../source/psnames.csv'


for ext in ('-Regular', '-Bold') :
	fontbase = 'Tagmukay' + ext
	font (target = process(fontbase + '.ttf', name('Tagmukay Beta'),
			cmd('hackos2 -q -u ' + os2bits + ' ${DEP} ${TGT}'),
			cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
		source = process('source/' + fontbase + '-source.ttf',
			cmd('../tools/FFchangeGlyphNames.py -i ' + psnames + ' ${DEP} ${TGT}')), #script from pysilfont
		version = TTF_VERSION,
		copyright = COPYRIGHT,
#		opentype = volt ( 'source/' + 'VOLT_' +  fontbase + '.vtp', no_make = 1),
		opentype = fea ( 'source/' +  fontbase + '.fea', no_make = 1),
		graphite = gdl ( 'source/Tagmukay.gdl', no_make = 1),
		script = ['tfng'],
		pdf = fret(),
		woff = woff('web/Tagmukay' + ext + '.woff', params = '-v ' + VERSION + ' -m ../source/Tagmukay-WOFF-metadata.xml'),
	)

def configure(ctx) :
    ctx.find_program('ttfautohint')
