# Steps

1) do `strings level03 | grep env`
2) substitute the `echo` command with a custom one by creating a script that calls `getflag` in the `/tmp` folder
3) change the `PATH` environment variable so that it overrides the default echo (`export PATH="folder/to/the/script:$PATH"`)
4) run again the executable
