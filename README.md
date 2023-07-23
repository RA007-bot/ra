# ra
termux-setup-storage
pkg update


pkg upgrade


pkg install python

pkg install git

rm -rf ra

pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests

git clone https://github.com/RA007-bot/ra

cd ra

python RA.py
