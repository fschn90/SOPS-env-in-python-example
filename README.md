# SOPS .env secrets in python script integration

This is an example on how to manage and deploy your secrets via sops and pgp encrypted into python scripts.

## dependencies

- sops
- gnupg
- pinentry

## requirements

pgp key [(generated with gnupg)](https://gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html) without passphrase (for ease of use in automatically executed python scripts, works just as well with passphase for pgp key). public pgp key added to .env file via [sops, readme here](https://raw.githubusercontent.com/getsops/sops/main/README.rst).

## installation

run `initial_setup.sh`

## run script

via `run.sh`
