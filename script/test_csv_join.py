import csv
import sys
from pathlib import Path


def csviter(pth):
    with open(pth, "r", newline="") as fp:
        r = csv.reader(fp)
        for i, line in enumerate(r):
            yield i, line


def check(stem):

    folder = Path(f"dati-{stem}")
    base = f"dpc-covid19-ita-{stem}"

    pth_all = folder / (base + ".csv")
    pth_single = sorted(folder.glob(base + "-????????.csv"))

    errors = 0
    r_all = csviter(pth_all)
    i, header = next(r_all)

    for pth in pth_single:
        r_sub = csviter(pth)
        _, head_sub = next(r_sub)
        assert head_sub == header
        for (j, line) in r_sub:
            i, line_t = next(r_all)
            if line_t != line:
                errors += 1
                print(
                    "{} (record {:d}) != {} (record {:d})".format(
                        pth_all, i, pth.stem, j
                    ),
                    file=sys.stderr,
                )
    assert len(list(r_all)) == 0
    return errors


def main():

    errors = 0
    for i in "province", "regioni", "andamento-nazionale":
        errors += check(i)

    if errors:
        sys.exit("\nFound {:d} error(s)".format(errors))


if __name__ == "__main__":
    main()
