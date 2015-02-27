#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Examines and argument and returns a boolean value:

    Args:
        kittens (int): Arg to be examined with a boolean and compared to another
        litterboxes (int): Arg to be compared to kittens and boolean
        catfood (bool): Arg to be combined with kittens

    Returns:
        Bool: A statement of truthiness for the Args in the statement

    Examples:

        >>>too_many_kittens(12, 12, False)
        True

        >>>too_many_kittens(13, 12, True)
        True
    """
    toomany = not (litterboxes >= kittens and catfood)
    return toomany
