
# You know that one meme where a guy spends 5 hours to automate a task that takes
#   5 minutes manually? Yeah I think I know where that time goes now.


# Anyways, the authentication for the next stage is a SSH private key, that one of two
# servers running on ports anywhere between 31000-32000 (inclusive) will give me if given
# the password to this level The other one will ping my pong.

current_level_pass=$(cat /etc/bandit_pass/bandit16)

ports=( 
    $(
        nmap --script ssl-cert -p 31000-32000 127.0.0.1 | 
        # the time goes into using a machine to generate human readable output, then trying to get the machine to understand itself.
        awk '/^\|/ && prev ~ /^[0-9]+\// {split(prev, a, "/"); print(a[1])} {prev=$0}'
    )
)

for p in "${ports[@]}"
do
    password_container=$( timeout 0.5 openssl s_client -crlf \
        -connect 127.0.0.1:$p \
        -servername 127.0.0.1 -quiet <<< "$current_level_pass" 2> /dev/null
    )
    if grep -q "$current_level_pass" <<< "$password_container"
        then continue
    fi
done

awk '/BEGIN OPENSSH PRIVATE KEY/,/END OPENSSH PRIVATE KEY/ {print $0}' <<< "$password_container"
