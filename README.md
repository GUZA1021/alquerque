# Alquerque with Minimax AI

First-semester programming project. A playable implementation of Alquerque,
a 5x5 board game, with a computer opponent using minimax search.
Two interfaces: text-based and graphical.

## Running

    python3 alquerque.py       # text interface, ASCII board
    python3 alquerqueGUI.py    # graphical interface (Tkinter)

Run from the project directory — the GUI loads its images from ./img/.
On launch you choose which sides the computer plays and how deep it
searches (1-7).

## Structure

| File | Contents |
|---|---|
| `board.py` | Board representation, legal move generation, move execution |
| `minimax.py` | Minimax search with alpha-beta pruning and position heuristics |
| `move.py` | Move datatype and accessors |
| `alquerque.py` | Text interface: game loop, ASCII rendering, input handling |
| `alquerqueGUI.py` | Tkinter interface (provided by the course) |

## The AI

`minimax.py` searches the game tree to a configurable depth. The heuristic in
`evaluate_state` scores captures, corner positions, and wins weighted by
remaining depth, so faster wins rank higher. When several moves tie for the
best score, one is chosen at random rather than always taking the first.

Alpha-beta pruning cut search time by roughly 83% in our benchmarks while
producing identical move sequences. An earlier version built an explicit tree
with dataclasses; it was replaced with direct recursion after it turned out to
allocate several hundred megabytes at higher depths.

## Technologies
Python, Tkinter

## Team
Group project by Lasse Møller Thomsen, Karim Adnan Amin and Asbjørn Piet
Sørensen. The Tkinter interface was provided by the course; the board logic,
the text interface and the minimax implementation are ours.

## Disclaimer
Developed for educational purposes as part of a university course.
