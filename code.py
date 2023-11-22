print("Starting")

# this is the code for layout for atreus keyboard using kmk firmware

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (board.GP0, board.GP1, board.GP9, board.GP3, board.GP4, board.GP12, board.GP8, board.GP7, board.GP15, board.GP6, board.GP5,)
keyboard.row_pins = (board.GP19, board.GP18, board.GP17, board.GP16,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
#   q     w     e     r     t       ||       y     u     i     o    p
#   a     s     d     f     g       ||       h     j     k     l    ;
#   z     x     c     v     b       ||       n     m     ,     .    /
#  esc   tab  super shift bksp ctrl || alt space  fn     -     '  enter


            [  # qwerty
        KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.NO,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,
        KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.NO,      KC.H,       KC.J,       KC.K,       KC.L,       KC.SCOLON,
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.LALT,   KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,
        KC.ESC,     KC.TAB,     KC.LGUI,    KC.LSHIFT,  KC.BSPACE,  KC.LCTRL,    KC.SPACE,   KC.MO(1),   KC.MINUS,   KC.QUOTE,   KC.ENTER,
    ],

#   !    @     up     {    }        ||     pgup    7     8     9    *
#   #  left   down  right  $        ||     pgdn    4     5     6    +
#   [    ]      (     )    &        ||       `     1     2     3    \
#  L2  insert super shift bksp ctrl || alt space   fn    .     0    =

            [  # fn layer
        KC.EXLM,    KC.AT,      KC.UP,      KC.LCBR,    KC.RCBR,    KC.NO,      KC.PGUP,    KC.N7,    KC.N8,    KC.N9,    KC.PAST,
        KC.HASH,    KC.LEFT,    KC.DOWN,    KC.RIGHT,   KC.DLR,     KC.NO,      KC.PGDN,    KC.N4,    KC.N5,    KC.N6,    KC.PLUS,
        KC.LBRC,    KC.RBRC,    KC.LPRN,    KC.RPRN,    KC.AMPR,    KC.LCTRL,   KC.GRV,     KC.N1,    KC.N2,    KC.N3,    KC.BSLASH,
        KC.TO(2),   KC.INS,     KC.LGUI,    KC.LSHIFT,  KC.BSPACE,  KC.LALT,    KC.SPACE,   KC.MO(1),   KC.PDOT,    KC.N0,    KC.EQL,
    ],

# insert home    ↑    end  pgup     ||       ↑     F7    F8    F9   F10
#   del   ←      ↓     →   pgdn     ||       ↓     F4    F5    F6   F11
#                          reset    ||             F1    F2    F3   F12
#             super shift bksp ctrl || alt space   L0
            [  # third layer
        KC.INS,     KC.HOME,    KC.UP,      KC.END,     KC.PGUP,    KC.NO,      KC.UP,      KC.F7,      KC.F8,      KC.F9,      KC.F10,
        KC.DEL,     KC.LEFT,    KC.DOWN,    KC.RIGHT,   KC.PGDN,    KC.NO,      KC.DOWN,    KC.F4,      KC.F5,      KC.F6,      KC.F11,
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.RESET,   KC.LCTRL,   KC.NO,      KC.F1,      KC.F2,      KC.F3,      KC.F12,
        KC.NO,      KC.NO,      KC.LGUI,    KC.LSHIFT,  KC.BSPACE,  KC.LALT,    KC.SPACE,   KC.TO(0),   KC.NO,      KC.NO,      KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
