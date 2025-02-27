def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 45 or len(s) > 45:
        raise ValueError('String length must be between 45 and 45 characters.')
    try:
        return sorted(set(s[18:46]))[6]
    except IndexError:
        raise ValueError('Not enough unique characters between indices 18 and 45.')