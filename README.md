# SOPS .env secrets in python script integration

This is an example on how to manage and deploy your .env secrets via sops and pgp encrypted into python scripts.

## dependencies

- sops
- gnupg
- pinentry

run `install_dependencies.sh` to install above dependencies for ubuntu. currently sops v3.8.1 is installed. please check [here](https://github.com/getsops/sops/releases) for latest release.

## requirements

pgp key [(generated with gnupg)](https://gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html) without passphrase (for ease of use in automatically executed python scripts, works just as well with passphase for pgp key). public pgp key added to .env file via [sops, readme here](https://raw.githubusercontent.com/getsops/sops/main/README.rst).

## installation

run `initial_setup.sh` to create python venv and install python dependencies.

## run script

via `run.sh` to ensure that venv is sourced.

## further reading:

- [SOPS Readme](https://raw.githubusercontent.com/getsops/sops/main/README.rst) on how to use sops.
- [python subprocesses](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module) on how subprocesses is used.
- [python-dotenv stream string into env](https://github.com/theskumar/python-dotenv?tab=readme-ov-file#parse-configuration-as-a-stream) on how stream works.
- [gupg and pgp](https://gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html) on how to generate and manage pgp keys.
