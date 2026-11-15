
# That's like the 2nd time I've had to copypaste logic.
# Seriously, should I build like a macro #include system like C has?

password_container=$(cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m')
IFS=" " read -r -a string_arr <<< "$password_container"
echo ${string_arr[-1]}

exit
