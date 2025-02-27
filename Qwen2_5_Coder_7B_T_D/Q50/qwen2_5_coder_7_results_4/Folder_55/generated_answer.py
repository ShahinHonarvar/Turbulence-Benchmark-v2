from collections import Counter

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = Counter()
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            anagrams[sorted_s] += 1
    for count in anagrams.values():
        if count >= 2:
            if count * (count - 1) // 2 >= 15:
                return True
    return False