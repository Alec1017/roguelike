#!/usr/bin/env python3
import tcod

from src.Action.MovementAction import MovementAction
from src.Action.EscapeAction import EscapeAction

from src.EventHandler import EventHandler

from config import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SET


def main() -> None:

    player_x = int(SCREEN_WIDTH / 2)
    player_y = int(SCREEN_HEIGHT / 2)

    event_handler = EventHandler()

    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=TILE_SET,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")
            
            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()