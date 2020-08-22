###############################################################################
# Copyright (C) 2018, 2019, 2020 Dominic O'Kane
###############################################################################

from FinTestCases import FinTestCases, globalTestCaseMode

import numpy as np
from financepy.market.volatility.FinEquityVolCurve import FinEquityVolCurve
from financepy.finutils.FinDate import FinDate

import sys
sys.path.append("..//..")

testCases = FinTestCases(__file__, globalTestCaseMode)

###############################################################################


def test_FinVolatilityCurve():

    valueDate = FinDate(2012, 6, 20)
    expiryDate = FinDate(2012, 12, 20)
    strikes = np.linspace(70, 130, 7)
    vols = np.array([0.23, 0.24, 0.267, 0.29, 0.31, 0.33, 0.35])
    polynomial = 5
    volCurve = FinEquityVolCurve(valueDate, expiryDate,
                                 strikes, vols, polynomial)

    interpStrikes = np.linspace(50, 150, 100)
    interpVols = volCurve.volatility(interpStrikes)

    if 1 == 0:
        import matplotlib.pyplot as plt
        plt.plot(strikes, vols, 'o', interpStrikes, interpVols)
        plt.show()

###############################################################################


test_FinVolatilityCurve()
testCases.compareTestCases()
