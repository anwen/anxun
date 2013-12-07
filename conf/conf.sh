sudo apt-get install git
sudo apt-get install make
sudo apt-get install curl
sudo apt-get install libcurl


sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install libcurl4-gnutls-dev # for pycurl

sudo pip install tornado
sudo pip install pycurl


mkdir /var/www/anxun -p
cd /var/www/anxun
git init .
git config receive.denyCurrentBranch ignore
git config --bool receive.denyNonFastForwards false
cd .git/hooks
# wget http://utsl.gen.nz/git/post-update
scp conf/post-update do:/var/www/anxun/.git/hooks # local
chmod +x post-update

# at local:
git remote add pro do:/var/www/anxun/
git push pro master
# after push
cd ../..
git checkout master


echo "export LC_ALL=en_US.UTF-8"  >>  /etc/profile
