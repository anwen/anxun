sudo apt-get install git


mkdir /var/www/anxun -p
cd /var/www/anxun
git init .
git config receive.denyCurrentBranch ignore
git config --bool receive.denyNonFastForwards false
cd .git/hooks
# wget http://utsl.gen.nz/git/post-update
scp conf/post-update do:/var/www/anxun/.git/hooks # local
chmod +x post-update
# after push
cd ../..
git checkout master

at local:
git remote rm pro
git remote add pro aaw:/var/www/anwen/
git push pro
