from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[sorted_s].append(s)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            for i in range(len(anagrams)):
                for j in range(i + 1, len(anagrams)):
                    if len(anagrams[i]) * len(anagrams[j]) >= 106:
                        return True
    return False