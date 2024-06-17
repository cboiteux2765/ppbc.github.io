loop_again=1

trap 'loop_again=0;wait' INT TERM

while (( loop_again )); do
    echo "Kill me with 'kill -9 $$'"
    ./qrcode.py &
    echo "Kill the Python script with 'kill $!'"
    wait
done