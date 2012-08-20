bllbrd.io Python client
=======================

This is a Python library that makes it even easier to talk the *bllbrd.io* 
web service in order to connect to the *bllbrd iPad app* (app storeapproval 
pending). 


Installation
------------

The code has been tested with Python 2.6 and 2.7.

Please use `pip` to install on your machine:

    pip install bllbrd


Getting Started
---------------

First, open the iPad app and create a channel. 

Then, in your Python code connect to that channel:

````python
from bllbrd import Channel
channel = Channel('my-channel-name')
````

And with one more line you can send e.g. a URL to your device:

````python
channel.post(type="url", url="http://code.pb.io/bllbrd/demo1.html")
`````


Different types of posts
------------------------

You can post all types of posts using the `channel.post()` method. Just
set the `type` argument to either `url`, `html` or `clear`, and supply
other parameters as keyword arguments.

````python
channel.post(type="url", url="http://code.pb.io/bllbrd/demo1.html")
channel.post(type="html", html="<h1>Hello world</h1>")
channel.post(type="clear")
````

Or use one of the following convenience methods:

### url

````python
channel.url("http://code.pb.io/bllbrd/demo1.html")
````

### html

````python
channel.html("<h1>Hello world!</h1>")
````

### clear

````python
channel.clear()
````


Customization
-------------

For the `url` and `html` post types you may supply one or more of the
following customization options:

### interactive

By default the user will not be able to interact with the content on the iPad. 
To enable touch interaction (links, buttons, etc.), set this to `True`.

* Type: `bool`
* Default: `False`
* Example: `channel.url("http://my-url.com/", interactive=True)`

### scrollable

If you want to make your content scrollable by the user, set this to `True`. 
Only useful if you also set `interactive=True`.

* Type: `bool`
* Default: `False`
* Example: `channel.url("http://my-url.com/", interactive=True, scrollable=True)`

### bounces

Set this to `True` if you want rubber-band scrolling on your content. Only make sense
in combination with `scrollable=True`.

* Type: `bool`
* Default: `False`
* Example: `channel.url("http://my-url.com/", interactive=True, scrollable=True, bounces=True)`

### zoomable

If you want the user to be able to use the pinch gestures to zoom the content,
set this to `True`.

* Type: `bool`
* Default: `False`
* Example: `channel.url("http://my-url.com/", zoomable=True)`

### javascript

Execute some arbitrary JavaScript code in the context of the web page after it's 
loaded.

* Type: `str`
* Default: `""`
* Example: `channel.url("http://my-url.com/", javascript="alert('Hello world!');")`

### ttl

By default the post content will stay on the screen until the user dismisses it or
the next post arrives. If you want your content to disappear after a specific time, 
set the `ttl` parameter to the desired time in seconds.

* Type: `float`
* Default: `-1` (do not disappear)
* Example: `channel.url("http://my-url.com/", ttl=5.0)`
