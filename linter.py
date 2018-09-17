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
import logging
from SublimeLinter.lint import Linter


logger = logging.getLogger('SublimeLinter.plugin.eslint')


class CFLint(Linter):
    """Provides an interface to CFLint."""

    syntax = ('coldfusioncfc', 'html+cfml', 'cfml')
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
    word_re = r'^<?(#?[-\w]+#?)'
    defaults = {
        'jar': '',
        '-configfile': ''
    }

    def cmd(self):
        jar = self.settings.get('jar')
        if not jar:
            logger.error(jar_file_missing_error_message)
            return None

        return [
            'java', '-jar', jar,
            '-stdin', '${file}',
            '-stdout',
            '-text',
            '-q',
            '${args}'
        ]


jar_file_missing_error_message = """
You MUST set the `jar` setting. It should point to your 'CFLint-*-all.jar'.
The absolute path is usually necessary unless this file is right in your working
dir.

E.g. for the global SublimeLinter settings:

    "linters": {
        "cflint": {
            "jar": "path/to/CFLint-1.4.0-all.jar"
        }
    }

In project settings, you would use something like this:

    "settings": {
        "SublimeLinter.linters.cflint.jar": "path/to/CFLint-1.4.0-all.jar"
    }

"""
