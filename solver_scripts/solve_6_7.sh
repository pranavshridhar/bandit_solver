

passwordfile=$(find / -user bandit7 -group bandit6 -size 33c 2> /dev/null)
cat $passwordfile
exit
