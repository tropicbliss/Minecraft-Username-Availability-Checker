#!/bin/bash

clear
echo "--> starting command tests"
if ! command -v python3 &> /dev/null
then
    echo "[error] python could not be found.. please make sure you have python installed."
    echo "For ubuntu you can run 'sudo apt-get install python3' to install python"
    exit
else
    echo "[ok] python detected | moving on..."
fi

if ! command -v git &> /dev/null
then
    echo "[error] git could not be found... please make sure you have git installed."
    exit
else
    echo "[ok] git detected | moving on..."
fi

echo ""
echo ""

if [ -d Minecraft-Username-Availability-Checker ]; then
    cd Minecraft-Username-Availability-Checker
elif [[ "${PWD##*/}" == "Minecraft-Username-Availability-Checker" ]]; then
    echo "[ok] you are already in Minecraft Username Availability Checker"
    echo ""
    echo ""
else
    echo "[ok] installing Minecraft Username Availability Checker..."
    git clone -q https://github.com/chronicallyunfunny/Minecraft-Username-Availability-Checker
    echo "[ok] installed Minecraft Username Availability Checker"
    cd Minecraft-Username-Availability-Checker
    echo ""
    echo ""
fi

if [ ! -e already_setup ]
then
    echo "[ok] installing requirements..."
    python3 -m pip install -q -r requirements.txt
    echo "[ok] successfully installed requirements!"
    echo > already_setup
    echo ""
    echo ""
fi

changed=0
git remote update && git status -uno | grep -q 'Your branch is behind' && changed=1
if [ $changed = 1 ]; then
    echo "[warning] Minecraft Username Availability Checker has a new update!"
    echo "updating Minecraft Username Availability Checker..."
    git pull -q
    echo "[ok] updated Minecraft Username Availability Checker..."
else
    echo "[ok] Minecraft Username Availability Checker is up to date!"
fi

if [ -n "$1" ]; then
clear
python3 check.py $1
else
    echo "[ok] Installation completed!"
fi
