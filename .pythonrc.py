def _init():

  import os

  from re import compile
  term_codes_re = compile(r"\033\[[^m]+m")

  term_codes = {
    'red'   : "\033[38;5;1m",
    'cyan'  : "\033[38;5;6m",
    'white' : "\033[38;5;7m",
    'green' : "\033[38;5;2m",
    'bold'  : "\033[1m",
    'off'   : "\033[0m",
  }

  def printable_len(text):

    tmp = term_codes_re.sub('', text)
    return len(tmp)

  virtual_env = os.environ.get('VIRTUAL_ENV')
  if (virtual_env is not None):
    venv = os.path.basename(virtual_env)
    border = term_codes['green']
    msg = "{edge} {bold}{white}Using virtual environment " \
          "'{red}{venv}{white}'{off} {edge}"
  else:
    venv = ''
    border = term_codes['cyan']
    msg = "{edge} Using {bold}{red}default{off} interpreter {edge}"

  fmt = dict(term_codes)
  fmt['border'] = border
  fmt['venv'] = venv
  fmt['edge'] = "{border}##{off}".format(**fmt)

  msg = msg.format(**fmt)
  fmt['header'] = "#" * printable_len(msg)

  header = "{border}{header}{off}".format(**fmt)

  print("")
  print(header)
  print(msg)
  print(header)
  print("")

_init()
del _init
