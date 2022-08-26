#!/bin/sh

DBFILE=Chinook_Sqlite.sqlite

wget -q https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/$DBFILE
md5sum $DBFILE
python -m sqlite2png $DBFILE
mv -v db.png Chinook_Sqlite.png
rm $DBFILE
