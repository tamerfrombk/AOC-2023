# AOC 2023

This is the [Advent of Code](https://adventofcode.com/) 2023 solutions written in Python.

## Requirements
- Python >= 3.11

## Quickstart

1. Sign into [Advent of Code](https://adventofcode.com/).
2. Get your session cookie using the Network Inspector in your browser. The cookie should be in the form `session=XYZ`.
3. Set `AOC_SESSION_COOKIE` environment variale to the `XYZ` part of your cookie.
4. Set up a virtual environment, source it, and install dependencies.

```sh
$ python -m virtualenv .venv
$ source .venv/bin/activate
(venv)$ pip install -r requirements.txt
```

5. Setup a new advent day: `./src/main.py setup 1`. This command will:
    1) Download the input file for that day into `src/day01/`.
    2) Setup a stub implementation file called `solution.py`.
6. Fill out the solutions in `solution.py`.
7. Solve: `./src/main.py solve 1`.
