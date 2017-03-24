#!/usr/bin/python
# encoding: utf-8

# set the default output folders
out="results"
DOCDIR="documentation"
OUTDIR="installers"
ZIPDIR="releases"
TESTDIR='tests'
TESTRESULTSDIR = 'tests'
STANDARDS = 'tests/standards'

# set the font name, version, licensing and description
APPNAME = 'Tagmukay'
VERSION = '2.000'
TTF_VERSION = '2.000'
COPYRIGHT='Copyright (c) 2006-2017 SIL International, all rights reserved'
LICENSE='OFL.txt'	
DESC_SHORT='Tifinagh Unicode TrueType font with OT and Graphite support'

DEBPKG = 'fonts-sil-tagmukay'


for ext in ('-Regular', '-Bold') :
	fbase = 'Tagmukay' + ext
	font (target = process('Tagmukay' + ext + '.ttf', name('Tagmukay Beta'),
                 cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
		source = 'source/' + fbase + '-nosmarts.ttf',
		version = TTF_VERSION,
		copyright = COPYRIGHT,
#		opentype = volt ( 'source/' + 'VOLT_' +  fbase + '.vtp', no_make = 1),
		opentype = fea ( 'source/' +  fbase + '.fea', no_make = 1),
		graphite = gdl ( 'source/Tagmukay.gdl', no_make = 1),
		script = ['tfng'],
		pdf = fret(),
		woff = woff(params = '-v ' + VERSION + ' -m ../source/Tagmukay-WOFF-metadata.xml'),
	)

def configure(ctx) :
    ctx.find_program('ttfautohint')

