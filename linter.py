#
# linter.py
# Linter for SublimeLinter 3, a code checking framework for Sublime Text 3
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

    syntax = ('coldfusioncfc', 'html+cfml', 'cfml')
    cmd = ['java', '${args}', '-file', '@', '-q', '-text']
    regex = r'''(?xi)
        # Severity
        ^\s*Severity:(?:(?P<warning>(WARNING|CAUTION|INFO|COSMETIC))|(?P<error>(FATAL|CRITICAL|ERROR)))\s*$\r?\n

        # Message code
        ^.*$\r?\n

        # File name
        ^.*$\r?\n

        # Column number
        ^\s*Column:(?P<col>\d+)\s*$\r?\n

        # Line number
        ^\s*Line:(?P<line>\d+)\s*$\r?\n

        # Message
        ^\s*Message:(?P<message>.+)$\r?\n

        # Variable
        ^.*$\r?\n

        # Expression
        ^.*$\r?\n
    '''
    multiline = True
    error_stream = util.STREAM_STDOUT
    word_re = r'^<?(#?[-\w]+#?)'
    tempfile_suffix = '-'
    defaults = {
        '-jar': '',
        '-configfile': ''
    }
