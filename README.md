# Ampyre - A simplistic battery monitor.

[Battery University](http://www.batteryuniversity.com) recommends that you charge your battery within a 40-80 % range for optimum performance and longevity. Ampyre frequently polls your current charge level to let you know if you're in the safe zone.

## Dependencies:

### Built-in Python modules:
* json - to read and write to config files.
* os - to check if a file exists.
* ~~subprocess - to spawn a new process.~~
* ~~shlex - lexical analyzers for simple syntaxes.~~ (removed in favor of [Python-Zenity](https://github.com/poulp/python-zenity)).

## Additional dependencies:
* [Python-Zenity](https://github.com/poulp/python-zenity)

## v0.0.1
* Rudimentary functionality.
* Needs to be run manually (not very useful at present).
* Depends (somewhat shakily) on *subprocess* without any way to accept user input.
* Generally unstructured code.

## v0.9.1
* Forewent (yes, that's a real word) reinventing the wheel by using [Python-Zenity](https://github.com/poulp/python-zenity).
* Added basic error handling.
* Added more dialogs (more interactive).
* Better config file handling.

# TODO
- [x] Remove shaky dependencies.
- [ ] Daemonize Ampyre.
- [ ] Figure out how to use with Cron (or cronie).
- [ ] Structure code better (follow a Python packaging guide).
