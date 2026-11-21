
# this has got to be the most i've ever used awk
# also -P is bad practice. revisit later because I am lazy.
strings data.txt | grep -P '=+ (?!the|password|is)' | awk -F' ' '{print $2}'

