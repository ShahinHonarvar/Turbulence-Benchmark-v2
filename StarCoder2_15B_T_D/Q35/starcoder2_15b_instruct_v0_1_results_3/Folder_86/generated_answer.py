def remove_repeat_chars(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    for char in freq:
        if freq[char] > 1 and 19 < string.index(char) < 32:
            string = string.replace(char, '')
    return string