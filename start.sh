if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/maharaja91/Forward-bot.git /Forward
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Forward
fi
cd /Forward
pip3 install -U -r requirements.txt
echo "Starting maharaja-forward-bot...."
python3 bot.py
