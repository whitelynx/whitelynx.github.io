#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

cd docs/.vuepress/dist

# if you are deploying to a custom domain
# echo 'www.example.com' > CNAME

git init
git add -A
git commit -m "deploy $(date -I)"

git push -f git@github.com:whitelynx/whitelynx.github.io.git master
