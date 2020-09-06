import sys
from pathlib import Path

import pandas as pd


def main():
    errors = 0
    try:
        for i in sorted(Path(".").rglob("*.csv")):
            try:
                df = pd.read_csv(i)
            except pd.errors.ParserError as exc:
                print(
                    "ParseError reading '{}': '{}'".format(i, str(exc).strip(),),
                    file=sys.stderr,
                )
                errors += 1
                continue
    except Exception as exc:
        sys.exit("Aborting: {}".format(exc))

    if errors:
        sys.exit("Found {:d} error(s)".format(errors))


if __name__ == "__main__":
    main()
