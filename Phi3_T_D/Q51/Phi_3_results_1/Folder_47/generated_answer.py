from collections import Counter

def if_contains_anagrams(strings):

    def clean_and_sort(s):
        cleaned = ''.join((c for c in s.lower() if c.isalpha()))
        return ''.join(sorted(cleaned))
    sorted_strings = {clean_and_sort(s): [] for s in strings}
    for s in strings:
        if len(s) >= 3:
            sorted_strings[clean_and_sort(s)].append(s)
    anagram_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in sorted_strings.values() if len(anagrams) > 1))
    return anagram_count <= 366