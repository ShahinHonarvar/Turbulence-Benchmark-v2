from collections import defaultdict

def if_contains_anagrams(strings):
    count_dict = defaultdict(int)
    anagram_count = 0
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            count_dict[key] += 1
    for count in count_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 66