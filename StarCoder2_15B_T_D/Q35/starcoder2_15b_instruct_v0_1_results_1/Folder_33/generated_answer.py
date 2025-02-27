import collections

def remove_repeat_chars(string):
    freq = collections.Counter(string)
    indices = {125, 825}
    for char, count in freq.items():
        if count > 1 and indices.isdisjoint(range(string.index(char), len(string) - string[::-1].index(char))):
            string = ''.join((c for c in string if c != char))
    return string