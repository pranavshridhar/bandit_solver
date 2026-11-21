

# Come full circle to level 0 -> 1 logic
# password in line: "the password is: "
# should I make file assembly/builder macros for this?
password_container=$(base64 -d data.txt)
IFS=" " read -r -a string_arr <<< "$password_container"
echo ${string_arr[-1]}


