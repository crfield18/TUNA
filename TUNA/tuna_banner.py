"""tuna_banner.py - ASCII art startup banner.

Requires: pip install termcolor
"""

from termcolor import colored


def print_banner():
    """Print the colored TUNA ASCII art banner to stdout."""
    banner = (
        colored(
            "\n      _______ _    _ _   _                     ___           \n"
            "     |__   __| |  | | \\ | |   /\\            __/__/__  _      \n",
            "white", force_color=True,
        )
        + colored(" ~~~~~~", "white", force_color=True)
        + colored(" | |  | |  | |  \\| |  /  \\", "white", force_color=True)
        + colored(" ~~~~~~~~", "white", force_color=True)
        + colored(" / .      \\/ ) ", "white", force_color=True)
        + colored("~~~~\n", "white", force_color=True)
        + colored(" ~~~~~~", "blue", force_color=True)
        + colored(" | |  | |  | | . ` | / /\\ \\", "white", force_color=True)
        + colored(" ~~~~~~", "blue", force_color=True)
        + colored(" (     ))    (", "white", force_color=True)
        + colored(" ~~~~~\n", "blue", force_color=True)
        + colored(" ~~~~~~", "blue", force_color=True)
        + colored(" | |  | |__| | |\\  |/ ____ \\ ", "white", force_color=True)
        + colored("~~~~~~", "blue", force_color=True)
        + colored(" \\___  ___/\\_) ", "white", force_color=True)
        + colored("~~~~", "blue", force_color=True)
        + colored(
            "\n        |_|   \\____/|_| \\_/_/    \\_\\          \\\\_\\           ",
            "white", force_color=True,
        )
    )
    print(banner)


if __name__ == "__main__":

    print_banner()
