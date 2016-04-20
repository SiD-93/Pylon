# Pylon - A simplistic battery monitor.

[Battery University](http://www.batteryuniversity.com) recommends that you charge your battery within a 40-80 % range for optimum performance and longevity. Pylon frequently polls your current charge level to let you know if you're in the safe zone.

## Dependencies:
### Python packages and/or modules.
* json - to read and write to config files.
* os - to check if a file exists.
* subprocess - to spawn a new process.
* shlex - lexical analyzers for simple syntaxes.
* Possibly more...

## v0.0.1
* Rudimentary functionality.
* Needs to be run manually (not very useful at present).
* Depends (somewhat shakily) on *subprocess* without any way to accept user input.
* Generally unstructured code.

# TODO
- [ ] Daemonize Pylon.
- [ ] Figure out how to use with Cron (or cronie).
- [ ] Structure code better.
- [ ] Remove shaky dependencies.
