glossolalia: Pseudo Po Translations
===================================


glossolalia is a GPL Licensed cli wrapper around the Psuedo Translations
available from Transifex_ pseudo translations. The available types are
``brackets``, ``unicode``, ``planguage``, ``extend``, and ``mixed``.

glossolalia is a fork of `potpie <https://github.com/dstufft/potpie>`_, which is
unmaintained.


Installation
------------

To install requests, simply: ::

    $ pip install glossolalia

Or, if you absolutely must: ::

    $ easy_install glossolalia

But, you really shouldn't do that.


Usage
-----

To create a pseudo translated po file, simply: ::

    $ glossolalia [--type] infile outfile

An example for a Django project might be: ::

    $ glossolalia locale/en/LC_MESSAGES/django.po locale/xx_pseudo/LC_MESSAGES/django.po

The default type is mixed, if you wish to use another type simplify specify it
as an option like: ::

    $ glossolalia --type brackets locale/en/LC_MESSAGES/django.po locale/xx_pseudo/LC_MESSAGES/django.po


Types
------

Brackets
    Adds square brackets around the string (e.g. [translated text])

Unicode
    Converts all characters into look alike unicode characters

PLanguage
    Increases the length of a string by around 30-50% by replacing the vowels with
    unicode chars that look alike.

    This is based on a P-language, which is a simple vowel-extending language.

Extend:
    Increases the length of a string by around 20-700% by appending special
    chars (Greek, Chinese, etc) to the end of the string.

Mixed:
    Combines Extend, Unicode and Brackets into one Type.

.. _Transifex: https://transifex.net/
