
password_file=$( \
    file ./* | \
    grep " ASCII text" \ # believe it or not, the space, however dirty of a trick it is, is VERY necessary.
    | awk -F: '{print $1}' \
)

cat $password_file
exit
