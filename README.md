shows-formatter
===============

A python script for standard conversion of TV show names.

The package formats the given show name, and uses a custom dictionary for special shows.

Usage
=====
Install the package as follows:

	$ python setup.py develop

Edit the shows map with your settings:

	$ vim showsformatter/shows_map.py

That's it.

The formatting function can be called as follows:

	from showsformatter import format_show
	
	format_show('spider man')
	>>> 'Spider-Man (1994)'
