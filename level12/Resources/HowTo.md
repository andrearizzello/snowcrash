# Steps

1) We check the file `level12.pl` and we see that there are two regex
 - The fist one turns the string into capital letters
 - The second one removes every characters after a space or tab
2) The thing is that we can't inject a command with a pipe as we did before so we need a file
3) Create a script in `/tmp` that pipe the output of `getflag` in a file with its name in uppercase like `/tmp/RUNME` or copy the one in the Resources folder
4) Make a http request with curl using this string "curl http://127.0.0.1:4646?x='`/*/RUNME`'" (this wildcard will look in every folder for the RUNME script)
4) Do a cat `/tmp/flag12` and get the flag