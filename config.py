import tcod


SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50
TILE_SET = tcod.tileset.load_tilesheet(
    'assets/tileset.png', 32, 8, tcod.tileset.CHARMAP_TCOD
)