import collections

def if_contains_anagrams(strings):
    length_count = collections.defaultdict(int)
    sorted_strings = {}
    for string in strings:
        length = len(string)
        if length >= 3:
            lowercase_string = string.lower()
            sorted_string = ''.join(sorted(lowercase_string))
            if length_count[sorted_string] < 2:
                length_count[sorted_string] += 1
                sorted_strings[sorted_string] = string
    anagram_count = sum((1 for count in length_count.values() if count > 1))
    return anagram_count <= 59