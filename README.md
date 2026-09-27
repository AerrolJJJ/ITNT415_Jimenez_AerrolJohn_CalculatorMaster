# Calculator Master

**Calculator Master :: Debug Dungeon** — a menu-driven, RPG-style Python calculator.

## Student Information

- **Student Name:** Aerrol John Jimenez
- **Course and Section:** S-ITNT415 | BIT42
- **GitHub Username:** AerrolJJJ
- **Project:** Midterm Summative Assessment

## Project Description

Calculator Master is a menu-driven Python calculator developed using Git and GitHub
branching, Pull Requests, and merge operations. It runs in the terminal and keeps showing
the menu until the user chooses to exit.

To make it more fun, the calculator has a "Debug Dungeon" theme: the user plays as an
IT-student hero, every calculation is a "skill", and each successful calculation gives XP
that levels the hero up (Intern → Junior Dev → Mid Dev → Senior Dev → Calculator Master).
Every screen is drawn inside a bordered box.

## Branch Structure

| Branch | Purpose |
|---|---|
| `main` | Stable branch. Holds the calculator skeleton and receives every merged feature. |
| `addition_Jimenez` | Addition feature (+) |
| `subtraction_Jimenez` | Subtraction feature (-) |
| `multiplication_Jimenez` | Multiplication feature (x) |
| `division_Jimenez` | Division feature (/) with division-by-zero handling |

```
main
 ├── addition_Jimenez
 ├── subtraction_Jimenez
 ├── multiplication_Jimenez
 └── division_Jimenez
```

## Program Features

- **Addition** — adds 2 to 10 numbers
- **Subtraction** — subtracts the second number from the first
- **Multiplication** — multiplies two numbers
- **Division** — divides the first number by the second
- **Input validation** — number prompts only accept real, finite numbers
- **Invalid input handling** — empty input, letters, `nan`/`inf` and out-of-range values are
  rejected with an error message and the program asks again
- **Invalid menu handling** — an unknown menu choice shows an `ERROR 404: SKILL NOT FOUND` box
- **Division-by-zero handling** — dividing by zero shows an error box instead of crashing
- **Continuous execution** — the menu keeps coming back after every operation
- **Exit option** — choose `0` to log out and see the final hero stats
- Extras: hero name, XP bar and levels, and a battle log of every calculation

## How to Run

Requires Python 3 (tested with Python 3.8 on Linux and 3.12 on Windows).

```
python3 calculator_master.py      # Linux / macOS
python calculator_master.py       # Windows
```

## Git Workflow

1. `main` was created first with the calculator skeleton (menu, borders, input validation,
   and a "locked" message for operations that were not built yet) and pushed to GitHub.
2. Each calculator operation was developed on its own feature branch, created from the
   updated `main`.
3. The changes were committed on the feature branch and pushed to GitHub.
4. A Pull Request was opened from the feature branch into `main` and reviewed.
5. After approval, the Pull Request was merged into `main` with a merge commit, and the next
   feature branch was started from the updated `main`.

## Commit History

Each feature branch contains at least two meaningful commits: one that implements the
operation and one that improves its validation, error handling, or output. The Pull Requests
were merged with merge commits, so every feature commit is still visible in the history of `main`.

## Sample Execution

Screenshots of the final calculator will be added here after all features are merged.
