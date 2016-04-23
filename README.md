# Ampyre - A simplistic battery monitor.

[Battery University](http://www.batteryuniversity.com) recommends that you charge your battery within a 40-80 % range for optimum performance and longevity. Ampyre frequently polls your current charge level to let you know if you're in the safe zone.

## Dependencies:

### Python Standard Library modules:
* json - to read and write to config files.
* os - to check if a file exists.
* ~~subprocess - to spawn a new process.~~
* ~~shlex - lexical analyzers for simple syntaxes.~~ (removed in favor of [Python-Zenity](https://github.com/poulp/python-zenity)).

## Additional dependencies:
* [Python-Zenity](https://github.com/poulp/python-zenity) (which in turn depends on [PyGTK](http://www.pygtk.org/))

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

## v0.9.3
* Recomposed modules (they were proving to be tedious).
* Much, much better config file handling. Now uses the default `~/.config` directory used by many GUI applications.
* More dynamic user support with use of environment variables.

# TODO
- [x] Remove shaky dependencies.
- [x] Setup config directories.
- [ ] Exception handling.
- [ ] Cron (use Python-Crontab) and/or Anacron.
- [ ] Weigh cron alternatives - [APScheduler](https://github.com/agronholm/apscheduler/), [Supervisor](https://github.com/Supervisor/supervisor), [Daemonize](https://github.com/thesharp/daemonize), and more.
- [ ] Structure code better (follow a Python packaging guide).
