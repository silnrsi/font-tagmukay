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

import os
tools = os.path.abspath('tools/')

for ext in ('-Regular', '-Bold') :
	fbase = 'Tagmukay' + ext
	font (target = process('Tagmukay' + ext + '.ttf', name('Tagmukay Beta'),
                 cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
		#process: changes designer glyph names (in source ttf) to Adobe glyph names which are in fea and gdl
		source = process('source/' + fbase + '-source.ttf',
				cmd('${FFCHANGEGLYPHNAMES.PY} -i ../source/psnames.csv ${DEP} ${TGT}')),
		version = TTF_VERSION,
		copyright = COPYRIGHT,
#		opentype = volt ( 'source/' + 'VOLT_' +  fbase + '.vtp', no_make = 1),
		opentype = fea ( 'source/' +  fbase + '.fea', no_make = 1),
		graphite = gdl ( 'source/Tagmukay.gdl', no_make = 1),
		script = ['tfng'],
		pdf = fret(),
		woff = woff('web/Tagmukay' + ext + '.woff', params = '-v ' + VERSION + ' -m ../source/Tagmukay-WOFF-metadata.xml'),
	)

def configure(ctx) :
    ctx.find_program('ttfautohint')
    ctx.find_program('FFchangeGlyphNames.py', path_list = tools) #script from pysilfont
