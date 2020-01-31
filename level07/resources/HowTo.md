# Steps

1) Using `strings level07` we can find the following functions being called: `system`, `asprintf`. we could also find the followning strings: `LOGNAME` `/bin/echo %s`
2) Edit the logname variable  logname with the following string `"\$(getflag)"`
3) Run `./level07`
