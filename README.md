`sqlite2png` tool generates .png image of database schema.

### Usage

From checkout without installing (needs `sqlalchemy` and `pydot`).
```bash
./sqlite2png.py sqlite.db
```
The diagram is written into `db.png`.

Install with pip and run as module.
```bash
pip install sqlite2png
python -m sqlite2png /usr/share/ibus-libpinyin/db/english.db
```
```
sqlite:////usr/share/ibus-libpinyin/db/english.db
writing db.png
```

![](examples/english.png)

### About and examples

`sqlite2png` is a CLI wrapper over
[`sqlalchemy_schemadisplay`](https://github.com/fschulze/sqlalchemy_schemadisplay)
lib by Florian Schulze, which uses `SQLAlchemy`, `pydot` and `graphviz`
under the hood. `Graphviz-cairo` is also recommended to improve image quality.

See [./examples](./examples).

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
