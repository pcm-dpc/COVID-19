import sys
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd

R_COLS = [
    "ricoverati_con_sintomi",
    "terapia_intensiva",
    "totale_ospedalizzati",
    "isolamento_domiciliare",
    "totale_positivi",
    "dimessi_guariti",
    "deceduti",
    "totale_casi",
]
R_COEFF = np.array(
    [
        [-1, -1, 1] + [0] * 5,
        [0] * 2 + [-1, -1, 1] + [0] * 3,
        [0] * 4 + [-1, -1, -1, 1],
    ]
)
R_COLS_INV = [[R_COLS[j] for j in c.nonzero()[0]] for c in R_COEFF]
assert np.linalg.matrix_rank(R_COEFF) == len(R_COEFF)


def read_csv(p):
    frame = pd.read_csv(
        p,
        encoding="UTF-8",
        na_values=[""],
        keep_default_na=False,
        parse_dates=["data"],
    )
    return frame


def check_inv_regioni(df):
    data = df[R_COLS].to_numpy()
    delta = R_COEFF @ data.T
    nz = delta.nonzero()
    return delta[nz], nz


def check_regioni(pth, regioni):

    delta, (invariant, ri) = check_inv_regioni(regioni)

    if len(delta) == 0:
        return 0

    print("\n* {}:".format(pth))
    for i in range(len(R_COEFF)):
        pos = invariant == i
        if np.count_nonzero(pos) == 0:
            continue
        regs = ri[pos]
        wrong = regioni.loc[regs, ["denominazione_regione"] + R_COLS_INV[i]].copy()
        assert (wrong.index == regs).all()
        wrong["*DELTA*"] = delta[pos]
        print(
            "  INVARIANT[{}] ERROR".format(i),
            textwrap.indent(
                wrong.to_string(
                    index=False,
                ),
                "  | ",
            ),
            sep="\n",
            file=sys.stderr,
        )

    return len(delta)


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
        sys.exit("\nFound {:d} error(s)".format(errors))


if __name__ == "__main__":
    main()
