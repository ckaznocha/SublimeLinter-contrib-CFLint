SublimeLinter-contrib-CFLint
================================

[![Build Status](https://travis-ci.org/ckaznocha/SublimeLinter-contrib-CFLint.svg?branch=master)](https://travis-ci.org/ckaznocha/SublimeLinter-contrib-CFLint)

This linter plugin for [SublimeLinter][docs] provides an interface to [CFLint](https://github.com/ryaneberly/CFLint). It will be used with files that have the “CFML” “CFC” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `CFLint` and `Sublimetext ColdFusion` are installed on your system.

To install `CFLint`, do the following:

1. Download `CFLint` 0.1.8 or newer from [ryaneberly/CFLint/releases](https://github.com/ryaneberly/CFLint/releases)
1. Extract all files
1. As of writing this the executlabe script files can be found in ./bin

**Note:** This plugin requires `CFLint` 0.1.8 or later.

To install `SublimeText ColdFusion`, do the following:

1. Follow the appropriate instructions from [SublimeText/ColdFusion](https://github.com/SublimeText/ColdFusion)

### Linter configuration
In order for `CFLint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `CFLint`, you can proceed to install the SublimeLinter-contrib-CFLint plugin if it is not yet installed.

On Mac OS X, to install `CFLint` into a location that can be found by SublimeLinter it is recommended that you place the contents of the zip file into a directory in /usr/local/lib/ called 'cflint' and then add a symbolic link in /usr/local/bin to the cflint execute file in /usr/local/lib/cflint/bin/. 

You will also need to make the cflint file in the bin directory executable if it is not already. To check this configuration has worked type 

`which cflint`

at the command prompt and you should get the response:

`/usr/local/bin//cflint`

You can also type `cflint` at the command prompt and make sure cflint executes and gives you the CLI help screen.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `CFLint`. Among the entries you should see `SublimeLinter-contrib-CFLint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
