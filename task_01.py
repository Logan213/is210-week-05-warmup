#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Performs arithmetic and returns a string.

    Args:
        wink (str): Arg to be multiplied by numwink.
        numwink=2 (int): Arg to multiply wink.

    Returns:
        str: All arguments concatenated with commas and added to a string.

    Examples:

        >>>know_what_i_mean(wink, 2)
        'Know what I mean? wink wink, nudge nudge'

        >>> know_what_i_mean('Hello ', 3)
        'Know what I mean? Hello Hello Hello, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
