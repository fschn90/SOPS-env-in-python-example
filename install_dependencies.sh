#!/bin/bash

curl -Lo sops.deb "https://github.com/getsops/sops/releases/download/v3.8.1/sops_3.8.1_amd64.deb"
sudo apt --fix-broken install ./sops.deb
rm -rf sops.deb
sudo apt install gnupg
