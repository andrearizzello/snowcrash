# Steps

1) Decompile the `getflag` executable (Using IDA for example https://www.hex-rays.com/products/ida/support/download_freeware.shtml)
2) Using IDA you will find a list of functions that calls `ft_des` with some encrypted hardcoded strings
3) Copying and jumping with `gdb` to the address of most of the function you will find the flag for each level
4) There is one flag bigger than the others, this will be the one we need
5) Log in as `flag14` with the password obtained
6) getflag