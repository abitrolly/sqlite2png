This is a command line interface for
[`sqlalchemy_schemadisplay`](https://github.com/fschulze/sqlalchemy_schemadisplay)
tool by Florian Schulze.

### Usage

From checkout without installing (needs `sqlalchemy` and `pydot`).
```bash
./sqlite2png.py sqlite.db
```

After installing with pip.
```bash
$ pip install sqlite2png
$ python -m sqlite2png /usr/share/ibus-libpinyin/db/english.db
sqlite:////usr/share/ibus-libpinyin/db/english.db
writing db.png
```

![](db.png)

The script uses SQLAlchemy, pydot and graphviz under the hood.
Graphviz-cairo is recommended upstream to improve image quality.

### Roadmap

* [ ] install command line script with `pip`
  * [ ] de-vendorize `sqlalchemy_schemadisplay` after it is released
* [ ] output .png to stdout
* [x] reproducuble .png (seems like it already is)
* [ ] option to show the image (needs PIL and image viewer)
* [ ] option to diff the image
* [ ] add example DB to the repo
* [ ] support full urls
```
    {py} postgres://user:pwd@host/database
    {py} sqlite:////usr/share/my.db
```
