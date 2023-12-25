#!/usr/bin/env python3

import sys
import os
import importlib.util
import requests

from pathlib import Path
from textwrap import dedent


def read_session_cookie() -> str:
    cookie = os.getenv("AOC_SESSION_COOKIE")
    if cookie is None:
        raise ValueError("set AOC_SESSION_COOKIE and try again")

    return cookie


def download_data_file(day: int, cookie: str) -> str:
    response = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input",
        headers={"cookie": f"session={cookie}"},
    )

    return response.text


def setup_source_file(src_dir: Path) -> None:
    src_dir.mkdir(parents=True, exist_ok=True)

    src_file = src_dir / "solution.py"
    if not src_file.exists():
        src_file.write_text(
            dedent(
                """
                   def solve1(input: str) -> None:
                       pass


                   def solve2(input: str) -> None:
                       pass
               """
            )
        )


def src_directory(day: int) -> Path:
    sday = str(day).zfill(2)

    return Path("src") / f"day{sday}"


def setup(day: int) -> None:
    # make sure we have a cookie before touching the file system
    cookie = read_session_cookie()

    src_dir = src_directory(day)
    setup_source_file(src_dir)

    with open(src_dir / "input.txt", "w") as f:
        data = download_data_file(day, cookie)
        f.write(data.strip())


# https://stackoverflow.com/a/67692
def load_solution_module(sday: str):
    module_name = f"src.day{sday}"
    spec = importlib.util.spec_from_file_location(
        module_name, f"src/day{sday}/solution.py"
    )
    assert spec
    assert spec.loader

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def solve(day: int) -> None:
    sday = str(day).zfill(2)
    solution = load_solution_module(sday)

    content = (src_directory(day) / "input.txt").read_text()
    print(solution.solve1(content))
    print(solution.solve2(content))


def parse_args(args: list[str]) -> tuple[str, int]:
    if len(args) != 3:
        raise ValueError(f"Usage: {args[0]} (setup|solve) [1..25]")

    cmd, day = args[1], int(args[2])
    if cmd not in ["setup", "solve"]:
        raise ValueError(f"command '{cmd}' is unrecognized")
    if day < 1 or day > 25:
        raise ValueError(f"day value '{day}' should be [1..25]")

    return cmd, day


def run(argv: list[str]) -> None:
    cmd, day = parse_args(argv)
    if cmd == "setup":
        setup(day)
    else:
        solve(day)


def main() -> None:
    try:
        run(sys.argv)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
