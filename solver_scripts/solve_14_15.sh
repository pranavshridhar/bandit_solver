
current_level_pass=$(cat /etc/bandit_pass/bandit14)

# Get 15's password by sending the password of 14 to localhost:30000
#    which of course we can only get by accessing the file only bandit14 has access to

# Also minimal netcat knowledge here
password_container=( $(nc 127.0.0.1 30000 <<< $current_level_pass) )
echo ${password_container[1]}
