import json
import sys
from pathlib import Path

import pandas as pd

PREFIX = "dpc-covid19-ita-"


def read_csv(pth):
    frame = pd.read_csv(
        pth,
        encoding="UTF-8",
        na_values=[""],
        keep_default_na=False,
    )

    return frame


def check_records(js, csv):
    errors = 0
    for i, (ra, rb) in enumerate(zip(js, csv)):
        if ra != rb:
            for k in rb:
                if ra.get(k) != rb[k]:
                    print(
                        "  | record #{}, field '{}':\n"
                        "  +->(json) {!r}\n"
                        "  +->(csv ) {!r}".format(i, k, ra.get(k), rb[k]),
                        file=sys.stderr,
                    )
                    errors += 1
    return errors


def main():

    errors = 0

    for stem in [
        "andamento-nazionale",
        "regioni",
        "province",
    ]:
        # json -> python list of dicts
        jpath = Path("dati-json").joinpath(PREFIX + stem).with_suffix(".json")
        try:
            with jpath.open("rb") as fp:
                json_py = json.load(fp)
        except json.JSONDecodeError as exc:
            print("\n* {}: JSON decode error: {}".format(jpath, exc), file=sys.stderr)
            errors += 1
            continue

        # CSV -> pandas DataFrame -> json -> python list of dicts
        # intermediate converson to json in order make direct comparison
        # of python data possible
        csvpath = Path("dati-" + stem).joinpath(PREFIX + stem).with_suffix(".csv")
        csv_df = read_csv(csvpath)
        csv_py = json.loads(csv_df.to_json(orient="records"))

        if len(json_py) != len(csv_py):
            print(
                "\n* {}: has {:d} records, expected {:d}".format(
                    jpath, len(json_py), len(csv_py)
                ),
                file=sys.stderr,
            )
            errors += 1
            continue

        if json_py != csv_py:
            print(
                "\n* {}: not compatible with {}".format(jpath, csvpath),
                file=sys.stderr,
            )
            errors += check_records(json_py, csv_py)

    if errors:
        sys.exit("\nFound {:d} errors".format(errors))


if __name__ == "__main__":
    main()
