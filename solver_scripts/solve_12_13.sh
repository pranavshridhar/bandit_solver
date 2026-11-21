
# FUUUUUUUUUUUUUUUUUUCK

# data.txt is a hexdump of a file that has been compressed again and again and again
# literally a masterclass in why one needs to learn scripting. I did this manually once and it 
# was like 12 or 13 layers deep

# Types of files we could be dealing with:
# - gzip: use gunzip
# - bzip2: use bunzip
# - tarchive: use tar -Oxf (boring)
# - ASCII file: target

# let's setup
tempdir=$(mktemp -d)
xxd -r data.txt > $tempdir/data0.out

cd $tempdir

count=0

# and just when I felt like I might actually enjoy bash scripting...
# ... I had to write an actual script in bash.
while ! file "data${count}.out" | grep -q "ASCII text"; do
    advcount=$((count + 1))
    if file "data${count}.out" | grep -q "gzip"; then # gzip path
        gunzip -c "data${count}.out" > "data${advcount}.out" # it's pronounced gunzip. not g-unzip.
    elif file "data${count}.out" | grep -q "bzip2"; then
        bunzip2 -c "data${count}.out" > "data${advcount}.out" # pronounced bunzip ditto ditto
    elif file "data${count}.out" | grep -q "tar archive"; then
        tar -Oxf "data${count}.out" > "data${advcount}.out"
    fi
    count=$((count + 1))
done

# TODO: Implement the damn macro. Figure that shit out. 3rd time in a row I've had to copy paste logic.
password_container=$(cat data${count}.out)
IFS=" " read -r -a string_arr <<< "$password_container"
echo ${string_arr[-1]}

