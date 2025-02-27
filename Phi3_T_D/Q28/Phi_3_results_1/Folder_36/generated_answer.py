def return_nth_smallest_ascii(s):
    try:
        chars = sorted(set(s[16:57]))
        return chars[8] if len(chars) > 8 else chars[0]
    except IndexError:
        return None