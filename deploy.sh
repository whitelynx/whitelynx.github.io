#!/usr/bin/env sh

# abort on errors
set -e

cd .vuepress
rm -r dist
git clone -b master $(git remote get-url origin) dist
cd ..

# build
npm run build

cd .vuepress/dist

# if you are deploying to a custom domain
# echo 'www.example.com' > CNAME

git add -A
git commit -m "deploy $(date -I)"
git push

# OLD: Only use the first time, or it will overwrite all previous deploy history!
#git init
#git add -A
#git commit -m "deploy $(date -I)"
#
#git push -f git@github.com:whitelynx/whitelynx.github.io.git master
