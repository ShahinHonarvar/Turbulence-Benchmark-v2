from collections import defaultdict

def if_contains_anagrams(strings):

    def count_sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = count_sorted_string(string)
        anagram_count[sorted_string] += 1
    return sum((1 for count in anagram_count.values() if count >= 2)) // 2 >= 108