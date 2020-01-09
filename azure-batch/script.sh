#!/bin/sh


env

echo
echo
echo

python compute_primes.py $M1 $M2 > output.txt

cat output.txt 

echo

