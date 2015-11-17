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

    syntax = ('coldfusioncfc', 'html+cfml')
    cmd = 'cflint -file @ -q -text'
    version_args = '-version'
    version_re = r'\b(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.8'
    regex = r'''(?xi)
        # The severity
        ^\s*Severity:(?:(?P<warning>(INFO|WARNING))|(?P<error>ERROR))\s*$\r?\n

        # The file name
        ^.*$\r?\n

        # The Message Code
        ^.*$\r?\n

        # The Column number
        ^\s*Column:(?P<col>\d+)\s*$\r?\n

        # The Line number
        ^\s*Line:(?P<line>\d+)\s*$\r?\n

        # The Error Message
        ^\s*Message:(?P<message>.+)$\r?\n
    '''
    multiline = True
    error_stream = util.STREAM_STDOUT
    word_re = r'^<?(#?[-\w]+)'
    tempfile_suffix = '-'
