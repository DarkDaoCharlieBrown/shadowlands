#!/usr/bin/env python

from asciimatics.renderers import StaticRenderer, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from tui.effect_materialize import Materialize
from tui.effect_cursor import Cursor
import sys
from tui import debug

#debug(self._screen._screen); import pdb; pdb.set_trace()

def menu(screen):

    # Typical terminals are 80x24 on UNIX and 80x25 on Windows
    #if screen.width != 80 or screen.height not in (24, 25):
    credstick_display = '''
╔═ Ledger Nano S ═══════════════════════════════════════╗
║
║  Address: 0xC579e6BF41789dEeF2E0AaCa8fBb8b0F0c762898
║
║  Ξth: 0.06040540066484375
║  Dai:
║
╚═══════════════════════════════════════════════════════╝
'''

    node='Connected to infura node at Geth/v1.8.13-patched-infura-omnibus-b59d4428/linux-amd64/go1.9.2'
    sync='[synced: block 6230988]\t\tNetwork: MainNet'
    pubterm='p u b l i c    t e r m i n a l\t\t\tv0 . 0 1'
    prompt='''Welcome, chummer.  Insert your credstick to begin...
A credstick, like a Trezor or a Ledger.   You know, what the bakebrains call a 'hardware wallet'. No creds, no joy, dataslave.
If you have cyberware installed in your finger I guess you could try plugging that in...
Or just keep hitting the enter button.  Have fun with that.'''

    loading_screen_effects = [
        Materialize(screen, StaticRenderer([node]), 0, 0),
        Materialize(screen, StaticRenderer([sync]), 0, 1, start_frame=10),
        Materialize(screen, FigletText('Shadowlands', 'slant'), 0, 3, signal_acceleration_factor=1.1, start_frame=15),
        Materialize(screen, StaticRenderer([pubterm]), 10, 10, signal_acceleration_factor=1.0005,start_frame=35),
        Cursor(screen, StaticRenderer([prompt]), 0, 14, start_frame=75),
        #Materialize(screen, StaticRenderer([_image]), 20, 20, Screen.COLOUR_GREEN, -0.005, 1.4)# , start_frame=0, stop_frame=5000),
        #UnicodeNoise( screen, BasicText(), stop_frame=300 ),
    ]

    main_menu_effects = [
        Materialize(screen, StaticRenderer([node]), 0, 0),
        Materialize(screen, StaticRenderer([sync]), 0, 1),
        Materialize(screen, StaticRenderer([credstick_display]), 0, 3)
    ] 

    scenes = [ 
        Scene(loading_screen_effects, -1, name="LoadingScreen"),
        Scene(main_menu_effects, -1, name="MainMenu"),
    ]

    screen.play(scenes, stop_on_resize=True)

while True:
    try:
        Screen.wrapper(menu)
        sys.exit(0)
    except ResizeScreenError:
        pass




'''
        self._plain_image = [" " * self._width for _ in range(self._height)]
        self._colour_map = [[(None, 0, 0) for _ in range(self._width)]
                            for _ in range(self._height)]
'''



