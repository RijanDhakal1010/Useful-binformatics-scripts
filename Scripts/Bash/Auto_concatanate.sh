#!/bin/bash
mkdir -p ~/Desktop/dump
for folder in *
do
    for file in $folder/*
    do
        test_name="${folder}.cat"
        cat $file/* > "/home/rijan/Desktop/dump/$test_name"
    done
done
echo "All the concatanated files are now in a desktop folder named dump and have the extension .cat" 