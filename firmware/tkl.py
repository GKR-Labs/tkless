from kmk.consts import LeaderMode, UnicodeMode
from kmk.handlers.sequences import compile_unicode_string_sequences as cuss
from kmk.handlers.sequences import send_string
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
import board

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.A0, board.A1, board.A2, board.A3, board.A4, board.A5, board.SCK, board.MOSI)
    row_pins = (board.D13, board.D2, board.D12, board.MISO, board.D11, board.RX, board.D10, board.TX, board.D9, board.SDA, board.D7, board.SCL)
    diode_orientation = DiodeOrientation.COLUMNS
    # rollover_cols_every_rows = 6?  2? idk 
keyboard = KMKKeyboard()

keyboard.debug_enabled = False
keyboard.unicode_mode = UnicodeMode.LINUX
keyboard.tap_time = 750

emoticons = cuss({
    # Emojis
    'BEER': r'πΊ',
    'BEER_TOAST': r'π»',
    'FACE_CUTE_SMILE': r'π',
    'FACE_HEART_EYES': r'π',
    'FACE_JOY': r'π',
    'FACE_SWEAT_SMILE': r'π',
    'FACE_THINKING': r'π€',
    'FIRE': r'π₯',
    'FLAG_CA': r'π¨π¦',
    'FLAG_US': r'πΊπΈ',
    'HAND_CLAP': r'π',
    'HAND_HORNS': r'π€',
    'HAND_OK': r'π',
    'HAND_THUMB_DOWN': r'π',
    'HAND_THUMB_UP': r'π',
    'HAND_WAVE': r'π',
    'HEART': r'β€οΈ',
    'MAPLE_LEAF': r'π',
    'POOP': r'π©',
    'TADA': r'π',
    'SHRUG_EMOJI': r'π€·',

    # Emoticons, but fancier
    'ANGRY_TABLE_FLIP': r'(γΰ² ηΰ² )γε½‘β»ββ»',
    'CELEBRATORY_GLITTER': r'+ο½‘:.οΎγ½(Β΄βο½‘)οΎοΎ.:ο½‘+οΎοΎ+ο½‘:.οΎγ½(*Β΄β)οΎοΎ.:ο½‘+οΎ',
    'SHRUGGIE': r'Β―\_(γ)_/Β―',
    'TABLE_FLIP': r'(β―Β°β‘Β°οΌβ―οΈ΅ β»ββ»',
})


keyboard.leader_mode = LeaderMode.ENTER
keyboard.leader_dictionary = {
    'atf': emoticons.ANGRY_TABLE_FLIP,
    'tf': emoticons.TABLE_FLIP,
    'fca': emoticons.FLAG_CA,
    'fus': emoticons.FLAG_US,
    'cel': emoticons.CELEBRATORY_GLITTER,
    'shr': emoticons.SHRUGGIE,
    'shre': emoticons.SHRUG_EMOJI,
    'poop': emoticons.POOP,
    'joy': emoticons.FACE_JOY,
    'ls': KC.LGUI(KC.HOME),  # Lock screen
    'cw': KC.LGUI(KC.END),  # Close window
    'dbg': KC.DBG,
}

_______ = KC.TRNS
xxxxxxx = KC.NO

keyboard.keymap = [
    [
#  0      1         2         3         4         5         6         7         0         1         2         3         4         5         6         7
KC.ESC,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   KC.PSCR,  KC.SLCK,  KC.PAUS, # 0-1
KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,  KC.EQL,   KC.BKSP,  KC.INS,   KC.HOME, #2-3 nb PGUP is at 7,7
KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,  KC.RBRC,  KC.BSLS,  KC.DEL,   KC.END, #4-5 nb PGDN is at 9,7
KC.CAPS,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,  KC.ENT,   xxxxxxx,  xxxxxxx,  KC.PGUP, # 6-7
KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     xxxxxxx,  KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,  xxxxxxx,  KC.UP,    KC.PGDN, # 8-9
KC.LCTL,  KC.LGUI,  KC.LALT,  xxxxxxx,  xxxxxxx,  KC.SPC,   xxxxxxx,  xxxxxxx,  xxxxxxx,  KC.RALT,  KC.MO(1), KC.APP,   KC.RCTL,  KC.LEFT,  KC.DOWN,  KC.RGHT, # 10-11
    ],
    [
_______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  
_______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  KC.MPLY,  KC.VOLU,  
_______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  KC.MSTP,  KC.VOLD,  
_______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  KC.MNXT,  
_______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  KC.MUTE,  
_______,  _______,  _______,  _______,  _______,  KC.LEAD,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  
    ]
]

if __name__ == '__main__':
    print("ready")
    keyboard.go()
