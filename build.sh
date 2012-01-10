#!/bin/sh

zip -x ".git/*" -x ".gitignore" -x "*/*.pyc" -x "build.sh" -x "*~" -r ../todotxt_plasmoid.plasmoid .
cd ..
plasmapkg -u todotxt_plasmoid
plasmoidviewer todotxt_plasmoid
