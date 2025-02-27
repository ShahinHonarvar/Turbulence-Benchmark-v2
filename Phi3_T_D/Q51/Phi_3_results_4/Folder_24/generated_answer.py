from collections import defaultdict

def if_contains_anagrams(strings):

    def string_signature(s):
        return ''.join(sorted(s.lower()))
    anagrams_map = defaultdict(list)
    for word in strings:
        if len(word) < 3:
            continue
        anagrams_map[string_signature(word)].append(word.lower())
    anagram_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagrams_map.values()))
    return anagram_count <= 96