# Server 52 asd
-- cai dat virtualenv
sudo apt-get install build-essential libssl-dev libffi-dev python-dev

-- python 3
sudo apt-get update
sudo apt install python3-pip
sudo apt install -y python3-venv
python3 -m venv env3

-- choose source
source env3/bin/activate

-- setup locust 
python3 -m pip install locustio

-- setup update slave sanic python 3
python3 -m pip install sanic

-- run master
locust --host=https://api-gateway.ranchers.xyz/ --locustfile=full_flow.py --master

-- run slave
python3 app_full_flow.py



# Setup python3 from source
## requiment & download source
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

cd /usr/src
sudo wget https://www.python.org/ftp/python/3.x.x/Python-3.x.x.tgz
sudo tar xzf Python-3.x.x.tgz

cd Python-3.7.4
sudo ./configure --prefix=/somewhere/else/than/usr/local
sudo make
sudo make install