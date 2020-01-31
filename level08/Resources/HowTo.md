# Steps

1) We try to launch the program with `token` as argument but we get the error `You may not access 'token'`
2) We create an empty file in `tmp` called `token` and we notice that we get the same error
3) We create a symbolic link called `/tmp/test` to `/home/user/level08/token` and we run the program with it as argument
4) We get the password for `flag08`
5) We log in as `flag08` and we run `getflag`
