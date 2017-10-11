from showsformatter.shows_map import SHOWS_MAP


def format_show(show_name):
    """
    Return the standard name for the given TV show.
    
    :param show_name: The show name to format.
    :return: The standard name.
    """
    # Search for show name in known shows map.
    fixed_show_name = show_name.lower().strip()
    if fixed_show_name in SHOWS_MAP:
        return SHOWS_MAP[fixed_show_name]
    # Make sure every word starts with a capital letter.
    return show_name.strip().title()
