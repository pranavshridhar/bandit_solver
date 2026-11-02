
# Solver script for Bandit level 0 -> 1

# Output: 'The password you are looking for is: (password here)'
password_container=$(grep password readme)
IFS=" " read -r -a string_arr <<< "$password_container"

echo ${string_arr[-1]}

exit
