# AlbiAPI

Simple API for usage with Polish social media site, albicla.com

## How to get started

To start using AlbiAPI, just install it using
```py
pip install albiapi
```
In Python, import it using
```py
from albiapi import *
```
And create client instance using the `AlbiclaClient()` class and log in
```py
client = AlbiclaClient(<e-mail>, <password>)
client.Login()
```
Now you can use AlbiAPI

To post something, use `client.Post(<post content>)`

And to search for an user, use `client.Search(<query>)`

`client.Search()` returns an JSON object looking something like this
```json
[
    {
        "name": "Albicla",
        "url": "@Albicla",
        "slug": "Albicla",
        "avatar": "\/uploads\/avatar\/1000000000_1611403859.jpg"
    },
    {
        "name": "\u00c5Albicla",
        "url": "@Albicla7",
        "slug": "Albicla7",
        "avatar": "\/data\/img\/no-avatar.png"
    }
]
```