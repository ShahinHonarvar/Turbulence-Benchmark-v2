from collections import defaultdict

def sorted_string(word):
    return ''.join(sorted(word.lower()))

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_count[sorted_string(string)] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) >= 81