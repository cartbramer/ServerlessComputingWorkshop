#!/bin/sh


env

echo
ls -l

echo
ls -l /

echo
echo

python /compute_primes.py $M1 $M2 > output.txt

cat output.txt 

echo

