#!/usr/bin/env python
"""
Custom loader for ptpython that incorporates an existing PYTHONSTARTUP
and enables per-venv history files. This code is based directly on the
launcher for ptpython.
"""

def run():

  import os
  import sys

  from ptpython.repl import embed, enable_deprecation_warnings, run_config

  # Create the config dir if it does not exist
  config_dir = os.path.expanduser(os.path.join('~', '.ptpython'))
  if (not os.path.isdir(config_dir) and not os.path.islink(config_dir)):
    os.mkdir(config_dir)

  # Add custom startup files to the starup path
  startup_paths = []
  startup = os.environ.get('PYTHONSTARTUP')
  if (startup is not None):
    startup_paths.append(startup)

  # Add the current directory to the Python path
  if sys.path[0] != '':
    sys.path.insert(0, '')

  enable_deprecation_warnings()

  # Run the ptpython configuration file
  def configure(repl):
    path = os.path.join(config_dir, 'config.py')
    # Handle unicode in case this is run by Python 2.7
    if (sys.version_info[0:2] < (3, 0)):
      path = path.decode('utf-8')
    if (os.path.exists(path)):
      run_config(repl, path)

  # Build a per-virtual-environment history file
  venv = os.environ.get('VIRTUAL_ENV')
  if (venv is None):
    hist_file = 'history'
  else:
    hist_file = 'history_{}'.format(os.path.basename(venv))

  # Start ptpython
  import __main__
  embed(vi_mode=False,
        history_filename=os.path.join(config_dir, hist_file),
        configure=configure,
        locals=__main__.__dict__,
        globals=__main__.__dict__,
        startup_paths=startup_paths,
        # Specify Unicode in case this is run by Python 2.7
        title=u'Python REPL (ptpython)')

if __name__ == '__main__':
  import sys
  sys.exit(run())
