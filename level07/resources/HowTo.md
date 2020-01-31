# Steps

1)using `strings level07` we can find the following functions being called: `system`, `asprintf`. we could also find the followning strings: `LOGNAME` `/bin/echo %s`
2) edit the logname variable  logname with the following string `"\$(getflag)"`
3)run `./level07`