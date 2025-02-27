from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagrams_count[count_chars(string)] += 1
    return sum((count * (count - 1) // 2 for count in anagrams_count.values())) <= 206