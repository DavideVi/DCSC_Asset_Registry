
apt-get update

# Web dev and server
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
apt-get install -y nodejs

# Database
apt-get -y install docker.io
docker run --name mongodb --restart=always -p 27017:27017 -d mongo
echo "export MONGODB_URI='localhost:27017/asset_registry'" >> /home/ubuntu/.bashrc

# Test environment
apt-get -y install python-pip
pip install selenium nose requests pymongo
echo "export AR_ENDPOINT='http://localhost:3000'" >> /home/ubuntu/.bashrc

# PhantomJS set-up
export PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
tar xvjf $PHANTOM_JS.tar.bz2
mv $PHANTOM_JS /usr/local/share
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

# Search engine CoreNLP
docker run --name corenlp --restart=always -p 9000:9000  -d motiz88/corenlp
