SublimeText Changelog
====================

v1.1.0 (2014-10-30)
-------------------

- Added support for folding based on startMarker only, the code will fold to the next startMarker or to the end of the document if there is none


v1.1.1 (2014-04-16)
-------------------

- fixed bug in setting package path for linux and mac (credit: mfkddcwy)


v2.0.0 (2017-01-02)
-------------------

- Active fold start and end markers are now selected by source syntax of the current file. These changes break compatability with the settings file of the previous versions. The user settings file must be updated. See default settings or README.md for details.


v2.1.0 (2017-04-18)
-------------------

- Added folding support to files containing `text` in their scope name, allowing HTML files to be folded (`text.html.basic` scope).