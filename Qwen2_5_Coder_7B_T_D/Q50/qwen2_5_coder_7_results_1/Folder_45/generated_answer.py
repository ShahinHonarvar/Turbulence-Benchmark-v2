from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            count = Counter([sorted_str for s in strings if len(s) >= 3 and sorted_str == ''.join(sorted(s.lower()))])
            anagram_count += count[sorted_str] * (count[sorted_str] - 1) // 2
    return anagram_count >= 277