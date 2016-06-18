sudo apt-get install cowsay
python makeTxts.py
python collectTxts.py
mv gre ~/gre
echo "shuf -n 1 ~/gre | cowsay" >> ~/.bashrc
rm -rf *.txt