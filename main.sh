sudo apt-get install cowsay
python makeTxts.py
python collectTxts.py
mv gre ~/wordlist
echo "shuf -n 1 ~/wordlist | cowsay" >> ~/.bashrc
rm -rf *.txt
