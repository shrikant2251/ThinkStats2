"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter
import numpy as np
import first
import thinkstats2
import operator

def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    freq_l = 0
    mode = 0
    for val,freq in hist.Items():
        if freq_l < freq:
           freq_l = freq
           mode = val
    return mode


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    dictVF = {}
    for val,freq in hist.Items():
       dictVF[val] = freq
    dictVF = dict(sorted(dictVF.items(), key=operator.itemgetter(1),reverse=True))
    res = np.array(list(dictVF.items()))
    print(res)
    return res

def light_heavy(firsts,others):
    print(firsts.totalwgt_lb.mean(),others.totalwgt_lb.mean())
    print(thinkstats2.CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb))
    return ""

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)
    
    light_heavy(firsts,others)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
