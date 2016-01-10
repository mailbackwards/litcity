# LitCity

### Description

[Visit on Hackdash](https://hackdash.org/projects/56912a1e62b2cc5d050af6d2)

Imagine walking down a city street and feeling that familiar buzz of a push notification. But instead of it being a notification on Twitter or a restaurant recommendation, it's a beautiful passage from a work of literature with a tie to that place.

In Paris, it could be walking past Cafe de Flore and receiving a sample from James Baldwin or Richard Wright. In Washington, DC, it could be a sample of an Alex Cross novel. In Japan, it could be one of Miyuke Miyabe's mystery novels. In Chicago, it could be a bit from Devil in the White City.

The core idea is to inject a little bit of romance and discoverability into books. Not only is the reader given a beautiful prompt to reflect upon (contributing to the mental environment) but it also is a wondrous reminder that literature lives wherever we are.

### Technical

LitCity consists of

- a Django app to manage book, quote, and location data
- a script to automatically extract and geolocate place names from text
- a script that fetches and stores book quotes from Goodreads

To set up, do the usual Django dance:

    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser

To start the server:

    $ python manage.py runserver

To create/edit data from the admin interface, go to /admin.

To run the scripts that add data:

    $ python manage.py import_locations {book_id} {csvfile}
    $ python manage.py get_top_quotes {book_title}  # fetches from Goodreads API

`import_locations` takes a CSV file with (label, latitude, longitude) columns.
`get_top_quotes` requires the title of a Goodreads book.

### Contributors

- Liam Andrew ([mailbackwards](http://github.com/mailbackwards))
- Helen Bailey ([hakbailey](http://github.com/hakbailey))
- Phil Polefrone ([prpole](http://github.com/prpole))
- Olimpia Estela ([olimpiaestela](http://github.com/olimpiaestela))
- Navraj Narula ([navierula](http://github.com/navierula))
- Danish Shabbir
