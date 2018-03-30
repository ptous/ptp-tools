## Tools for use with `ptpython`

### About `ptpython`
To learn about ptpython and why it's cool and useful, check out its [git
homepage](https://github.com/jonathanslenders/ptpython).

### About These Tools
I like testing code in a REPL interpreter. The Python REPL is quite nice
(at least when full readline support is active), but ptpython is far nicer.

Unfortunately, to use it with a Python virtual environment, you normally need
to either install it in your global Python site-packages, or install it in
a the Python virtual environment you're working in. Either approach can be
inconvenient, depending on what you're working on and whether any of its
packages conflict with those used by ptpython. When developing in a virtual
environment, installing ptpython there likely means your virtual environment
contains libraries that aren't necessary to the project you are working
on, which is not ideal.

That's the main problem these tools solve. It provides the following features.

* The ability to start `ptpython` without installing it in the active
  virtual environment. There are some caveats on this - see below.
* The ability to work with both Python 2.7 and 3.x virtual environments.
* A distinct REPL history file _per virtual environment_.
* An optional message reminding you what virtual environment (if any) you have
  active when you start a a REPL (plain `python` or `ptpython`).

To work in this way, ptpython is installed as a stand-alone library
directory and made accessible by adding its location to the PYTHONPATH
environment variable.

### Installing These Tools

Grab the latest `install_ptp_tools.bin` file from the [github release
page](https://github.com/ptous/ptp-tools/releases/latest). Alternatively,
clone the repo and create the installer yourself using the `build_sfx.sh`
script.

Run `install_ptp_tools.bin` script. It will ask you where you want to install
the `ptpython` libraries. The default location is `~/opt/ptpython/site-lib`.
It doesn't matter where it's installed, as long as you have write access to
that location.

The installer will also prompt you for the location of script files needed to
launch ptpython through this tool. The default location is `~/bin/ptpython`.

When everything else is done, the script will give you instructions on how to
update your shell profile script to add the tools to you PATH, based on where you installed it. By default, that would be the following line. (The example assumes you use `bash` as a shell.)

```bash
export PATH=~/bin/ptpython:$PATH
```

If you also want to use the virtual environment message for REPLs, add this as
well.

```bash
export PYTHONSTARTUP=~/bin/ptpython/.pythonrc.py
```

### Starting `ptpython`
Once all the above steps are done, you should be able to start an interactive
ptpython session by running the command `ptp`. Why not use `ptpython`? Well,
for one thing, `ptp` is shorter, but mainly I didn't want to mask any actual
installs of ptpython on the PATH. If you don't like the name `ptp` (I can
easily imagine that name colliding with other tools), feel free to rename or
symlink it.

### Caveats
As mentioned above, ptpython depends on a number of other packages. When
you run ptpython with another Python virtual environment active, ptpython's
virtual environment's package paths will come first (have higher priority) when
Python loads packages. If your virtual environment uses any of the same
libraries as ptpython, and you use different versions, then ptpython may cause
your code to run with different versions of packages than you expect. Of course,
this only affects code you run within the ptpython REPL.

Similarly, if you set a PYTHONPATH, your settings will have a higher priority
than the library path for ptpython. If your PYTHONPATH contains  conflicting
versions of libraries used by ptpython, then ptpython may not work correctly.

When it starts, the `ptp` command tries to determine if `ptpython` is already
installed in your current (virtual) environment. If it is, `ptp` will defer to
your environment for ptpython's libraries rather than using its own installed
version.

### History Files
History files are stored in `~/.ptpython`. The normal history file is simply
named `history`. The virtual-environment-specific history files are named
`history-$VIRTUAL_ENV`. There is no explicit cleanup of these files, so if
you create and delete virtual environments often, you may end up with a lot
of "orphaned" history files.

This also means that the history will persist even if you delete and recreate a
virtual environment with the same name. This may or may not be what you want.
Putting them somewhere else, like in the virtual environment directory, would
not be very hard. It can be changed by editing the `ptp.py` script installed
alongside `ptp`.

### Upgrading `ptpython`
If you want to upgrade the version of ptpython used by the `ptp` script,
just run the following command: `ptp --upgrade`. This will use the pip currently
on your `PATH` but will use it to explicitly reinstall/upgrade ptpython in the
path selected for its libraries during the installation of these tools. It won't
change your current Python environment's installed site libraries, even if
`ptpython` is installed there.

### Bugs and Issues

If you find any bugs or have suggestions, feel free to open an issue on GitHub.

This bundle has been tested on Ubuntu 16.04 and CentOS 6/7.

It's possible some of the switches I've used with certain commands won't work
on macOS systems. If so, let me know and I'll look for more compatible ways
to achieve the same effect.
