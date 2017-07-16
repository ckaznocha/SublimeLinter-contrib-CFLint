SublimeLinter-contrib-CFLint
================================

[![Build Status](https://travis-ci.org/ckaznocha/SublimeLinter-contrib-CFLint.svg?branch=master)](https://travis-ci.org/ckaznocha/SublimeLinter-contrib-CFLint)

This linter plugin for [SublimeLinter 3][docs] provides an interface to [CFLint](https://github.com/cflint/CFLint). It will be used with files that have the “CFML” “CFC” syntax.

## Installation
**SublimeLinter 3** must be installed in order to use this plugin. If **SublimeLinter 3** is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that **CFLint** and **SublimeText-CFML** are installed on your system.

To install **CFLint**, do the following:

1. Download latest Java SE 8+ [JRE](https://www.java.com/en/download/manual.jsp) or [JDK](http://www.oracle.com/technetwork/java/javase/downloads/index-jsp-138363.html) if you plan to build it yourself.
1. Download latest **CFLint** standalone JAR (`CFLint-1.0.1-all.jar` or newer) from [cflint/CFLint/releases](https://github.com/cflint/CFLint/releases) or [Maven repository](http://search.maven.org/#search%7Cga%7C1%7Ccflint). Alternatively, build it yourself using [these instructions](https://github.com/cflint/CFLint/wiki/How-Do-I-Install-This-Tool%3F).

To install **SublimeText-CFML**, do the following:

1. Follow the instructions from [jcberquist/sublimetext-cfml](https://github.com/jcberquist/sublimetext-cfml).

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `cflint`. Among the entries you should see `SublimeLinter-contrib-CFLint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how **SublimeLinter 3** works with settings, please see [Settings][settings]. For information on standard linter settings, please see [Linter Settings][linter-settings].

### Plugin-specific settings
- `jar_file` (_required_): This must contain the absolute path to the `CFLint-*-all.jar` file.
- `config_file_name` (_optional_): This must contain just the file name for the **CFLint** config file. [default: `cflintrc.xml`]
- `aux_config_dirs` (_optional_): An array of paths that will act as auxiliary directories for the config file if not found in the project being linted.

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
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
