# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
#| output: false
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt;import stata_setup
stata_setup.config('/Applications/Stata', 'mp')
#
#
#
#| echo: false
#| output: false
cd "/Users/shaokangyang/Documents/Stata"
clear all
set maxvar 120000, permanently
set more off

import delimited "/Users/shaokangyang/Library/CloudStorage/GoogleDrive-shaokang@vt.edu/My Drive/Nethealth/Data/CNSA/combine/7/df7_1.5r.csv"
gen date2 = date(date, "YMD")
#
#
#
#| echo: false
#| output: false
import stata_setup
stata_setup.config('/Applications/Stata', 'mp')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
