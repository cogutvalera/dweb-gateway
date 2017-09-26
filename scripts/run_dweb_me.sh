#!/bin/bash

PIPS="multihash py-dateutil redis base58 pynacl"
cd /usr/local/dweb_gateway
pip3 install --disable-pip-version-check -U $PIPS
[ -d data ] || mkdir data
git commit -a -m "Changes made on server" && git push
git checkout deployed # Will run server branch
git pull
git merge origin/deployable
git commit -a -m "merged" && git push
if [ ! -f data/idents_files_urls_sqlite ]
then
	curl -L -o data/idents_files_urls_sqlite.gz https://archive.org/download/ia_papers_manifest_20170919/index/idents_files_urls.sqlite.gz
	gunzip data/idents_files_urls_sqlite.gz
fi
#cd python
if ps -ef | grep ServerGateway | grep -v grep
then
	echo "You need to kill that process above first"
else
    echo "Starting Server "
    python3 -m python.ServerGateway &
    ps -ef | grep ServerGateway | grep -v grep
fi


