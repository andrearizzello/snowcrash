# Steps

1) We notice the `echo "..pass.." | sha1sum` string
2) We inject the code in the echo `$(getflag) > /tmp/password`
3) We read the file that contains the flag in `/tmp/password`