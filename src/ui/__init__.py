from . import (
    cli,
    wsfastapi
)

STRATEGY_HIGH_ORDER = {
    'cli': cli,
    'ws': wsfastapi
}


def create_app(ui_module: str):
    return STRATEGY_HIGH_ORDER[ui_module]
