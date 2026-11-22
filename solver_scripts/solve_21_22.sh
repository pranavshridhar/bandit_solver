
# I have a hard time believing that the cronjob for getting to 22
#   can be anything other than cronjob_bandit22.

# TODO: This works but this code can be optimized. Good opportunity to learn bash functions.
script_file=$(cat /etc/cron.d/cronjob_bandit22 | sed -n '1p' | awk '{print $3}')
password_file=$(cat $script_file | sed -n '3p' | awk '{print $4}')
cat $password_file
