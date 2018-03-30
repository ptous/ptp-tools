#!/bin/bash

function _die() {
  echo "${1:-Unspecified error}"
  exit ${2:-1}
}

FILES_TO_ARCHIVE=(
  ptp
  ptp.py
  .pythonrc.py
)

TARBALL=$(TMPDIR='/tmp' mktemp)

tar cz "${FILES_TO_ARCHIVE[@]}" > "$TARBALL" || _die "Error creating archive!"

cat install_ptp_tools.sh_tpl "$TARBALL" > install_ptp_tools.bin || \
  _die "Error concatenating installer and archive!"

chmod u+x install_ptp_tools.bin
