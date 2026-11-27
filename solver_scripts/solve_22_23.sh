
# This is going to be a bit more direct than dynamically trying to find a file.
# As such, this is going to assume that the setup stays the same until the end of time

targetfile=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
cat /tmp/$targetfile

