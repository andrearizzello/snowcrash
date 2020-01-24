# Steps

1) Scan the filsystem from the root with `find -user flag00 2> /dev/null`
2) Do a cat of one of the two files that you get on the output
3) go on `https://www.dcode.fr/caesar-cipher` and put the output you got before (shift 15 or do a bruteforce)
4) Do `su - flag00` and put the dcode.fr output as password
5) do `getflag`
