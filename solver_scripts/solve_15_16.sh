
current_level_pass=$(cat /etc/bandit_pass/bandit15)

# ooo this was a tough one. Not using SSL but finding a way to get the output back
password_container=( 
    $(openssl s_client -crlf \
    -connect 127.0.0.1:30001 \
    -servername 127.0.0.1 -quiet <<< $current_level_pass) )

echo ${password_container[-1]}

