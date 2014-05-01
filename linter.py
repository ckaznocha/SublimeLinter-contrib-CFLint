#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by ckaznocha
# Copyright (c) 2014 ckaznocha
#
# License: MIT
#

"""This module exports the CFLint plugin class."""
from SublimeLinter.lint import Linter, util

class CFLint(Linter):

    """Provides an interface to CFLint."""

    syntax = ('coldfusioncfc','html+cfml')
    cmd = ('cflint -q -text -file')
    regex = r'''(?xi)
        ^\s*Column:(?P<col>\d+)$\r?\n
        ^\s*Line:(?P<line>\d+)$\r?\n
        ^\s*message:(?P<message>.+)$
    '''
    multiline = True
    tempfile_suffix = '-'