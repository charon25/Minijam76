import util

WIDTH = 1280
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_TITLE = "MiniJam76"
FRAME_INTERVAL = 16

###CHEMINS
RESOURCES_PATH = "resources/"
TEXTURES_PATH = RESOURCES_PATH + "textures/"



###NEUTRONS
NEUTRON_SIZE = 25
NEUTRON_SPEED = 10
NEUTRON_PATH = TEXTURES_PATH + "neutron.png"
NEUTRON_CREATION_ANGLE_U = 30
NEUTRON_CREATION_ANGLE_PU = 50
NEUTRON_MAX_BOUNCES = 3

###ATOMES
#TAILLES
KR93_SIZE = SR94_SIZE = 40
ZR103_SIZE = 41
XE134_SIZE = 45
XE140_SIZE = BA140_SIZE = 46
U234_SIZE = U235_SIZE = 54
U236_SIZE = U237_SIZE = U238_SIZE = U239_SIZE = NP237_SIZE = NP238_SIZE = NP239_SIZE = PU238_SIZE = PU239_SIZE = 55
#TEXTURES
KR93_PATH = TEXTURES_PATH + "kr93.png"
SR94_PATH = TEXTURES_PATH + "sr94.png"
ZR103_PATH = TEXTURES_PATH + "zr103.png"
XE134_PATH = TEXTURES_PATH + "xe134.png"
XE140_PATH = TEXTURES_PATH + "xe140.png"
BA140_PATH = TEXTURES_PATH + "ba140.png"
U234_PATH = TEXTURES_PATH + "u234.png"
U235_PATH = TEXTURES_PATH + "u235.png"
U236_PATH = TEXTURES_PATH + "u236.png"
U237_PATH = TEXTURES_PATH + "u237.png"
U238_PATH = TEXTURES_PATH + "u238.png"
U239_PATH = TEXTURES_PATH + "u239.png"
NP237_PATH = TEXTURES_PATH + "np237.png"
NP238_PATH = TEXTURES_PATH + "np238.png"
NP239_PATH = TEXTURES_PATH + "np239.png"
PU238_PATH = TEXTURES_PATH + "pu238.png"
PU239_PATH = TEXTURES_PATH + "pu239.png"
#TEMPS DE DESINTEGRATION
U237_DECAY = 2000
U239_DECAY = 2000
NP238_DECAY = 2000
NP239_DECAY = 2000
PU239_DECAY = 2000
DECAY_MAX_SHAKE = 5
#FISSION
ATOM_CREATION_ANGLE_MIN = 60
ATOM_CREATION_ANGLE_MAX = 85
ATOM_CREATION_SPEED_FACTOR = 0.3
#TYPE U235
U235_NEUTRON = 0
U235_SRXE2 = 1
U235_KRBA3 = 2
#AUTRES
ATOM_BRAKE = 0.01


###JOUEUR
ARROW_COLOR = (255, 0, 0)
ARROW_WIDTH = 10
LEFT_CLICK = 1
RIGHT_CLICK = 3
MIN_DISTANCE_TO_PLAY = 40




















