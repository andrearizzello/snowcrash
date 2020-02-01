# Steps

1) If we lauch the program we see that `level13` checks for the UID so we have to override the function
2) Copy the `libcoverride.c` into `/tmp`
3) Compile it with `gcc -shared -o /tmp/libcoverride.so /tmp/libcoverride.c`
4) Launch gdb with `LD_PRELOAD` set like this `LD_PRELOAD=/tmp/libcoverride.so gdb ./level13`
5) type `r` and get the flag