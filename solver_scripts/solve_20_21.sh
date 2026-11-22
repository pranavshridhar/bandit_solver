
current_level_pass=$(cat /etc/bandit_pass/bandit20)

# Hehe
# Also I am too afraid of what prints to terminal goddamn
(nc -l -p 42069 <<< $current_level_pass) & 
sleep 0.5 # since we are concurrent we need to ensure order of ops
./suconnect 42069 | sed -n '3p'
