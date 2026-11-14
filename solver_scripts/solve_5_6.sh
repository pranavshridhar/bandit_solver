
# target file is human readable, not executable, and is 1033 bytes in size.
# they really should have made more files that are 1033 bytes in size just to throw me off
# because it should not be this easy
# TODO: if somehow they find this repo and take my advice, implement 

password_file=$(find . -size 1033c)
cat $password_file
exit

# file type is ASCII text, with very long lines, so let python strip the whitespace downstream
