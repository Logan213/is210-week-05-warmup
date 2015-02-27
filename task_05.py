#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function comparing to arguments"""


def defaults(my_required, my_optional=True):
    """Examines argument and returns a boolean value:

    Args:
        my_required (mixed): Arg to be compared to another arg
        my_optional (mixed): Arg to be compared to my_required with True
        default value

    Returns:
        Bool: A statement declaring truthiness of statement

    Examples:

        >>>defaults(True)
        True

        >>>defaults(True, False)
        False
    """
    logic = my_optional is my_required
    return logic
