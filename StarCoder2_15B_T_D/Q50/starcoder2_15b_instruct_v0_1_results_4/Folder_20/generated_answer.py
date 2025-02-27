def if_contains_anagrams(strings):
    anagrams_count = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    return any((count >= 64 for count in anagrams_count.values()))

def get_anagrams_count(string):
    sorted_string = ''.join(sorted(string.lower()))
    return anagrams_count.get(sorted_string, 0)