import sys
import textwrap
from pathlib import Path

import pandas as pd


def read_csv(p):
    frame = pd.read_csv(
        p,
        encoding="UTF-8",
        na_values=[""],
        keep_default_na=False,
        parse_dates=["data"],
    )
    return frame


def _inv_regioni_0(regioni):
    delta = regioni.totale_casi - (
        regioni.totale_positivi + regioni.dimessi_guariti + regioni.deceduti
    )
    err = delta != 0
    if err.any():
        wrong = regioni.copy()[err][
            [
                "denominazione_regione",
                "totale_casi",
                "totale_positivi",
                "dimessi_guariti",
                "deceduti",
            ]
        ]
        wrong["*DELTA*"] = delta
        return wrong


def _inv_regioni_1(regioni):
    delta = regioni.totale_positivi - (
        regioni.totale_ospedalizzati + regioni.isolamento_domiciliare
    )
    err = delta != 0
    if err.any():
        wrong = regioni.copy()[err][
            [
                "denominazione_regione",
                "totale_positivi",
                "totale_ospedalizzati",
                "isolamento_domiciliare",
            ]
        ]
        wrong["*DELTA*"] = delta
        return wrong


def _inv_regioni_2(regioni):
    delta = regioni.totale_ospedalizzati - (
        regioni.ricoverati_con_sintomi + regioni.terapia_intensiva
    )
    err = delta != 0
    if err.any():
        wrong = regioni.copy()[err][
            [
                "denominazione_regione",
                "totale_ospedalizzati",
                "ricoverati_con_sintomi",
                "terapia_intensiva",
            ]
        ]
        wrong["*DELTA*"] = delta
        return wrong


def check_regioni(pth, regioni):
    errors = 0
    wrong = _inv_regioni_0(regioni)
    if wrong is not None:
        print(
            "* {}: INVARIANT ERROR 0".format(pth),
            textwrap.indent(wrong.to_string(index=False), "  | "),
            sep="\n",
            file=sys.stderr,
        )
        errors += len(wrong)
    wrong = _inv_regioni_1(regioni)
    if wrong is not None:
        print(
            "* {}: INVARIANT ERROR 1".format(pth),
            textwrap.indent(wrong.to_string(index=False), "  | "),
            sep="\n",
            file=sys.stderr,
        )
        errors += len(wrong)
    wrong = _inv_regioni_2(regioni)
    if wrong is not None:
        print(
            "* {}: INVARIANT ERROR 2".format(pth),
            textwrap.indent(wrong.to_string(index=False), "  | "),
            sep="\n",
            file=sys.stderr,
        )
        errors += len(wrong)

    return errors


def main():
    errors = 0

    # check dati-regioni
    for pth in sorted(
        Path("dati-regioni").glob("dpc-covid19-ita-regioni-????????.csv")
    ):
        try:
            df = read_csv(pth)
        except pd.errors.ParserError as exc:
            print(
                "ParseError reading '{}': '{}'".format(
                    pth,
                    str(exc).strip(),
                ),
                file=sys.stderr,
            )
            errors += 1
            continue
        errors += check_regioni(pth, df)

    if errors:
        sys.exit("Found {:d} error(s)".format(errors))


if __name__ == "__main__":
    main()
