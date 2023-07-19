from rich import box
from rich.panel import Panel
from rich.console import Console
from Colours import colours


def info_panel(information, colour):
    """red = error, blue = information, green = affirmative action"""
    console = Console()
    panel = ""
    panel = Panel(
        information,
        style=colours[colour],
        box=box.SIMPLE_HEAD
    )
    console.print(panel)