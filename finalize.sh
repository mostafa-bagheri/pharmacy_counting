#!/bin/bash
git remote set-url origin https://github.com/mostafa-bagheri/pharmacy_counting.git
read -p "Comment: " cm

git add -A
git commit -am "$cm"
git push origin master
