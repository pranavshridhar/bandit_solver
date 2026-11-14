
# The password is in a dir called inhere and is the only human readable file.

password_file=$( \
    file ~/inhere/* | \
    grep " ASCII text" | \
    awk -F: '{print $1}' \
)

cat $password_file
exit
