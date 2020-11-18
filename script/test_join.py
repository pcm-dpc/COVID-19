import csv
import sys
from pathlib import Path


def csviter(pth, header):
    with open(pth, "r", newline="") as fp:
        r = csv.reader(fp)
        if header != next(r):
            raise ValueError("bad header")
        for line in r:
            yield line


def check(stem):

    folder = Path(f"dati-{stem}")
    base = f"dpc-covid19-ita-{stem}{{}}.csv".format

    pth_all = folder / base("")
    pth_single = sorted(folder.glob(base("-????????")))

    errors = 0
    with open(pth_all) as fp:
        csv_total = enumerate(csv.reader(fp), start=1)
        i, header = next(csv_total)

        for pth in pth_single:
            sub = csviter(pth, header)
            for j, line in enumerate(sub, start=2):
                i, line_t = next(csv_total)
                if line_t != line:
                    errors += 1
                    print(
                        "{} (record {:d}) != {} (record {:d})".format(
                            pth_all, i, pth.stem, j
                        ),
                        file=sys.stderr,
                    )
    return errors


def main():

    errors = 0
    for i in "province", "regioni", "andamento-nazionale":
        errors += check(i)

    if errors:
        sys.exit("\nFound {:d} error(s)".format(errors))


if __name__ == "__main__":
    main()
