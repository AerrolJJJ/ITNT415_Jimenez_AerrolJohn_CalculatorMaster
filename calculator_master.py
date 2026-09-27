# ==============================================================
#   CALCULATOR MASTER :: DEBUG DUNGEON
#   A menu-driven RPG-style calculator
# --------------------------------------------------------------
#   Student : Aerrol John Jimenez
#   Course  : S-ITNT415   |   Section: BIT42
#   Project : Midterm Summative Assessment
# --------------------------------------------------------------
#   Feature branches:
#     addition_Jimenez        -> Addition        (+)
#     subtraction_Jimenez     -> Subtraction     (-)
#     multiplication_Jimenez  -> Multiplication  (x)
#     division_Jimenez        -> Division        (/)
# ==============================================================

import math
import os
import sys
import textwrap

# make sure the box-drawing characters print correctly on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# os.system("") turns on ANSI colors in the Windows terminal
os.system("")
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

BOX_WIDTH = 46          # inside width of every bordered box
XP_PER_WIN = 10         # XP earned every time a skill succeeds
XP_PER_LEVEL = 50       # XP needed to level up
MAX_NAME_LENGTH = 12

RANKS = ["Intern", "Junior Dev", "Mid Dev", "Senior Dev", "Calculator Master"]

# player data for this session
hero = {"name": "", "level": 1, "xp": 0}
battle_log = []


# ==============================================================
#   UI HELPERS
# ==============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(f"\n{BLUE}Press ENTER to return to the dungeon...{RESET}")


def draw_box(lines, title="", color=CYAN):
    """Print lines of text inside a double-line border."""
    print(color + "╔" + "═" * (BOX_WIDTH + 2) + "╗")
    if title:
        print("║ " + title.center(BOX_WIDTH) + " ║")
        print("╠" + "═" * (BOX_WIDTH + 2) + "╣")
    for line in lines:
        # long lines get wrapped so the right border never breaks
        # (wrap("") gives an empty list, so blank lines stay as spacers)
        for part in textwrap.wrap(line, BOX_WIDTH) or [""]:
            print("║ " + part.ljust(BOX_WIDTH) + " ║")
    print("╚" + "═" * (BOX_WIDTH + 2) + "╝" + RESET)


def format_number(value):
    """Show 42 instead of 42.0 and add commas to big numbers."""
    if value.is_integer():
        return f"{int(value):,}"
    return f"{round(value, 6):,}"


def term(value):
    """Put negative numbers in () so equations stay readable."""
    if value < 0:
        return f"({format_number(value)})"
    return format_number(value)


# ==============================================================
#   HERO STATS
# ==============================================================

def get_rank():
    index = min(hero["level"], len(RANKS)) - 1
    return RANKS[index]


def xp_bar():
    filled = hero["xp"] * 10 // XP_PER_LEVEL
    return "[" + "#" * filled + "-" * (10 - filled) + "]"


def gain_xp():
    hero["xp"] += XP_PER_WIN
    print(f"{GREEN}  +{XP_PER_WIN} XP earned!{RESET}")
    if hero["xp"] >= XP_PER_LEVEL:
        hero["xp"] -= XP_PER_LEVEL
        hero["level"] += 1
        draw_box([f"{hero['name']} is now Lv.{hero['level']} - {get_rank()}!"],
                 "LEVEL UP!", YELLOW)


def add_to_log(entry):
    battle_log.append(entry)


# ==============================================================
#   INPUT VALIDATION
# ==============================================================

def get_number(prompt):
    """Keep asking until the user types a real number."""
    while True:
        raw = input(f"{YELLOW}{prompt}{RESET}").strip()
        if raw == "":
            print(f"{RED}  SyntaxError: input is empty. Try again, hero.{RESET}")
            continue
        try:
            number = float(raw)
        except ValueError:
            print(f"{RED}  SyntaxError: '{raw}' is not a number. Try again, hero.{RESET}")
            continue
        if not math.isfinite(number):
            print(f"{RED}  ValueError: '{raw}' is not allowed in this dungeon.{RESET}")
            continue
        return number


def get_hero_name():
    """Ask for a hero name that fits inside the status box."""
    while True:
        name = input(f"{YELLOW}Enter your hero name: {RESET}").strip()
        if name == "":
            print(f"{RED}  A hero needs a name!{RESET}")
        elif len(name) > MAX_NAME_LENGTH:
            print(f"{RED}  Too long! Max {MAX_NAME_LENGTH} characters.{RESET}")
        elif not name.replace(" ", "").isalnum():
            print(f"{RED}  Letters and numbers only, please.{RESET}")
        else:
            return name


# ==============================================================
#   SKILLS (each one is built on its own feature branch)
# ==============================================================

def locked_skill(skill_name):
    draw_box([f"{skill_name} is still being coded on its feature "
              "branch. Check back after the merge!"],
             "[LOCKED]", YELLOW)


# [addition_Jimenez] Addition
def add(a, b):
    return a + b


def addition_skill():
    draw_box(["Add two numbers together."], "[1] ADDITION (+)", GREEN)
    a = get_number("  First number : ")
    b = get_number("  Second number: ")
    result = add(a, b)

    equation = f"{term(a)} + {term(b)} = {format_number(result)}"
    draw_box([equation, "", f"Sum: {format_number(result)}"],
             "ADDITION RESULT", GREEN)
    add_to_log(f"Addition: {equation}")
    gain_xp()


# ==============================================================
#   SCREENS
# ==============================================================

def title_screen():
    clear_screen()
    draw_box([
        "",
        "      \\   /",
        "    --(o o)--      A wild BUG appeared!",
        "      / ^ \\",
        "",
        "Welcome, IT student. The Debug Dungeon is crawling "
        "with bugs and only math can stop them. Every "
        "calculation is a skill, and every correct answer "
        "gives you XP.",
        "",
        "Coded by Aerrol John Jimenez | BIT42",
        "S-ITNT415 Midterm Summative Assessment",
        "",
    ], "CALCULATOR MASTER :: DEBUG DUNGEON", MAGENTA)


def show_menu():
    clear_screen()
    draw_box([
        f"Hero: {hero['name']}   Lv.{hero['level']} {get_rank()}",
        f"XP  : {xp_bar()} {hero['xp']}/{XP_PER_LEVEL}",
        "",
        "  [1] Addition          (+)",
        "  [2] Subtraction       (-)",
        "  [3] Multiplication    (x)",
        "  [4] Division          (/)",
        "  [5] View Battle Log",
        "  [0] Logout (Exit)",
    ], "CALCULATOR MASTER :: DEBUG DUNGEON")


def show_battle_log():
    if len(battle_log) == 0:
        lines = ["No battles yet. Go squash some bugs!"]
    else:
        lines = []
        for number, entry in enumerate(battle_log, start=1):
            lines.append(f"{number}. {entry}")
    draw_box(lines, "BATTLE LOG", BLUE)


def logout():
    draw_box([
        f"Hero    : {hero['name']}",
        f"Rank    : Lv.{hero['level']} {get_rank()}",
        f"XP      : {xp_bar()} {hero['xp']}/{XP_PER_LEVEL}",
        f"Battles : {len(battle_log)}",
        "",
        "Thanks for playing. See you next sprint!",
    ], "LOGGED OUT", MAGENTA)


# ==============================================================
#   MAIN PROGRAM LOOP
# ==============================================================

def main():
    title_screen()
    hero["name"] = get_hero_name()

    while True:
        show_menu()
        choice = input(f"{YELLOW}>> Choose your skill [0-5]: {RESET}").strip()

        if choice == "1":
            addition_skill()
        elif choice == "2":
            locked_skill("Subtraction")
        elif choice == "3":
            locked_skill("Multiplication")
        elif choice == "4":
            locked_skill("Division")
        elif choice == "5":
            show_battle_log()
        elif choice == "0":
            logout()
            break
        else:
            draw_box([f"Unknown command: '{choice}'",
                      "Valid commands are 0, 1, 2, 3, 4 and 5."],
                     "ERROR 404: SKILL NOT FOUND", RED)
        pause()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{RED}Connection lost... the hero escaped the dungeon.{RESET}")
