def return_nth_smallest_ascii(s):
    start = 29
    end = 33
    assert len(s) > end, 'String is too short'
    selection = s[start:end + 1]
    chars = list(selection)
    chars.sort(key=lambda c: ord(c))
    return chars[4]