#!/usr/bin/env python3

import os

import sqlalchemy
# vendored until 1.4 is released
from v140dev_sqlalchemy_schemadisplay import create_schema_graph


def save_to_png(dburl, outpng):
    print(dburl)

    # create the pydot graph object by autoloading all tables via a bound metadata object
    if dburl.startswith('sqlite:///'):
        # open SQLite databases read-only
        # https://github.com/sqlalchemy/sqlalchemy/issues/4863
        import sqlite3
        def connectro():
            filepath = dburl[10:]
            sqliteurl = 'file:' + filepath + '?mode=ro'
            return sqlite3.connect(sqliteurl, uri=True)

        from sqlalchemy import create_engine
        metadata = sqlalchemy.MetaData(create_engine('sqlite://', creator=connectro))
    else:
        metadata = sqlalchemy.MetaData(dburl)

    graph = create_schema_graph(
        metadata=metadata,
        show_datatypes=False,  # The image would get nasty big if we'd show the datatypes
        show_indexes=False,    # ditto for indexes
        rankdir='LR',          # From left to right (instead of top to bottom)
        concentrate=False      # Don't try to join the relation lines together
    )
    print('writing {}'.format(outpng))
    graph.write_png(outpng)    # write out the file


def cli():
    usage = '''\
usage: {py} <db.sqlite>

saves database diagram into db.png
'''.format(py=__file__)

    import sys
    if not sys.argv[1:]:
        print(usage)
        sys.exit()

    arg_db = sys.argv[1]
    if os.path.isfile(arg_db):
        dburl = 'sqlite:///' + arg_db
    else:
        dburl = arg_db

    pngname = 'db.png'
    sys.exit(save_to_png(dburl, pngname))


if __name__ == '__main__':
    cli()
