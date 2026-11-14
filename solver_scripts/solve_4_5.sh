
# The password is in a dir called inhere and is the only human readable file.

password_file=$( \
    file ~/inhere/* | \
    # space is VERY necessary to cut out "extended-ASCII text". Easier to define whhat you want than what you don't want.
    grep " ASCII text" | \
    awk -F: '{print $1}' \
)

cat $password_file
exit
