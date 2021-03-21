import pygame as pyg
import co

#FOND
BACKGROUND_TEXTURE = pyg.image.load(co.BACKGROUND_PATH)
#MENU
MENU_TEXTURE = pyg.image.load(co.MENU_PATH)
#FIN NIVEAU
EOL_TEXTURE = pyg.image.load(co.EOL_PATH)

#NEUTRON
NEUTRON_TEXTURE = pyg.image.load(co.NEUTRON_PATH)
#ELECTRON
ELECTRON_TEXTURE = pyg.image.load(co.ELECTRON_PATH)

#ATOMES
KR93_TEXTURE = pyg.image.load(co.KR93_PATH)
SR94_TEXTURE = pyg.image.load(co.SR94_PATH)
ZR103_TEXTURE = pyg.image.load(co.ZR103_PATH)
XE134_TEXTURE = pyg.image.load(co.XE134_PATH)
XE140_TEXTURE = pyg.image.load(co.XE140_PATH)
BA140_TEXTURE = pyg.image.load(co.BA140_PATH)
U234_TEXTURE = pyg.image.load(co.U234_PATH)
U235_TEXTURES = [pyg.image.load(path) for path in co.U235_PATHS]
U236_TEXTURE = pyg.image.load(co.U236_PATH)
U237_TEXTURE = pyg.image.load(co.U237_PATH)
U238_TEXTURE = pyg.image.load(co.U238_PATH)
U239_TEXTURE = pyg.image.load(co.U239_PATH)
NP237_TEXTURE = pyg.image.load(co.NP237_PATH)
NP238_TEXTURE = pyg.image.load(co.NP238_PATH)
NP239_TEXTURE = pyg.image.load(co.NP239_PATH)
PU238_TEXTURE = pyg.image.load(co.PU238_PATH)
PU239_TEXTURE = pyg.image.load(co.PU239_PATH)