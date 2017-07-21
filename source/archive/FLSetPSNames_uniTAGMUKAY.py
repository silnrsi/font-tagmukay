#FLM: FL Set PSnames - Adobe names (Tagmukay)

import PSNames_uni

#dict to handle unencoded glyphs
sil_to_adobe_name_dict = {
".null" : "uni0000",
"LtnSmA.alt" : "a.alt",
"LtnSmAGrave.alt" : "agrave.alt",
"LtnSmAAcute.alt" : "aacute.alt",
"LtnSmACircum.alt" : "acircumflex.alt",
"LtnSmATilde.alt" : "atilde.alt",
"LtnSmABreve.alt" : "abreve.alt",
"LtnSmADiaer.alt" : "adieresis.alt",
"LtnSmARingAbv.alt" : "aring.alt",
"LtnSmG.alt" : "g.alt",
"TifLtrSILa" : "uni2D300302",
"TifLtrSILe" : "uni2D620302",
"TifLtrSILi" : "uni2D620323",
"TifLtrYal.slant" : "uni2D4D.slant",
"TifLtrYan.slant" : "uni2D4F.slant",
"TifLtrSILo" : "uni2D670302",
"TifLtrSILschwa" : "uni2D300306",
"TifLtrSILu" : "uni2D530302",
"TifLigTuarElta" : "uni2D4D2D7F2D5C",
"TifLigTuarEnda" : "uni2D4F2D7F2D39",
"TifLigTuarEnfa" : "uni2D4F2D7F2D3C",
"TifLigTuarEnja" : "uni2D4F2D7F2D4C",
"TifLigTuarEnja.alt" : "uni2D4F2D7F2D4C.alt",
"TifLigTuarEmta" : "uni2D4E2D7F2D5C",
"TifLigTuarEfta" : "uni2D3C2D7F2D5C",
"TifLigTuarEnza" : "uni2D4F2D7F2D64",
"TifLigTuarEnfta" : "uni2D4F2D7F2D3C2D7F2D5C",
"TifLigTuarEnta" : "uni2D4F2D7F2D5C",
"TifLigTuarEngha" : "uni2D4F2D7F2D57",
"TifLigTuarEnga" : "uni2D4F2D7F2D36",
"TifLigTuarEmba" : "uni2D4E2D7F2D40",
"TifLigTuarEmsa" : "uni2D4E2D7F2D59",
"TifLigTuarEsta" : "uni2D592D7F2D5C",
"TifLigTuarErta" : "uni2D542D7F2D5C",
"TifLigTuarEnsa" : "uni2D4F2D7F2D59",
"TifLigTuarEnka" : "uni2D4F2D7F2D3E",
"TifLigTuarEshta" : "uni2D5B2D7F2D5C",
}

#rename glyphs to Adobe names

for g in fl.font.glyphs:
	if g.unicode:
		PSnm = PSNames_uni.make_PSNm(g.name, g.unicode)
	else:
	    if sil_to_adobe_name_dict.has_key(g.name):
	        PSnm = sil_to_adobe_name_dict[g.name]
	    else:
	        print "glyph %s has no PS name specified" % g.name
	        continue
	g.name = PSnm
	fl.UpdateGlyph(g.index)

fl.UpdateFont()
