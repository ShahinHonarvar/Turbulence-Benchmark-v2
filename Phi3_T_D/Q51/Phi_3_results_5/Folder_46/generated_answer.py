from collections import defaultdict

def if_contains_anagrams(strings):

    def alphabet_position(s):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagrams[alphabet_position(string)].append(string)
    count = 0
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 61