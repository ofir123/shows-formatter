from showsformatter.shows_map import SHOWS_MAP


def format_show(show_name):
    """
    Return the standard name for the given TV show.
    
    :param show_name: The show name to format.
    :return: The standard name.
    """
    # Remove brackets group name prefix.
    if show_name.startswith('[') and ']' in show_name:
        show_name = show_name.split(']')[1]
    # Search for show name in known shows map.
    fixed_show_name = show_name.lower().strip()
    if fixed_show_name in SHOWS_MAP:
        return SHOWS_MAP[fixed_show_name]
    # Make sure every word starts with a capital letter.
    return show_name.strip().title()
