Taiga contrib Ping Federate auth
=========================

The Taiga plugin for Ping Federate authentication

Installation
------------

### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-ping-federate-auth` with:

```bash
  pip install taiga-contrib-ping-federate-auth
```

Modify your settings/local.py and include the line:

```python
  INSTALLED_APPS += ["taiga_contrib_ping_federate_auth"]
```

### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-ping-federate-auth` compiled code:

```bash
  cd dist/plugins/
  svn export "https://github.com/allan-simon/taiga-contrib-ping-federate-auth/trunk/front/dist" "auth"

```
Download in your `dist/images/contrib` directory of Taiga front the `taiga-contrib-ping-federate-auth` google icon:

```bash
  cd dist/images/contrib
  wget "https://raw.googleusercontent.com/taigaio/taiga-contrib-google-auth/stable/front/images/contrib/google-logo.png"
```

Include in your dist/conf.json in the contribPlugins list the value `"/plugins/auth/ping_federate_auth.json"`:

```json
...
    "contribPlugins": ["/plugins/auth/ping_federate_auth.json"]
...
```

Running tests
-------------

3/12/15: PLEASE NOTE: These tests were just copied from the github plugin and are not yet operational.  They will be updated shortly.

We only have backend tests, you have to add your taiga-back directory to the
PYTHONPATH environment variable, and run py.test, for example:

```bash
  cd back
  add2virtualenv /home/taiga/taiga-back/
  py.test
```
