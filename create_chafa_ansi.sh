#!/bin/bash
clear
chafa "./assets/frames/frame012.png" --symbols block --colors 256 --size 120x50 > "./assets/ansi/frame012.ansi"
cat "./assets/ansi/frame012.ansi"