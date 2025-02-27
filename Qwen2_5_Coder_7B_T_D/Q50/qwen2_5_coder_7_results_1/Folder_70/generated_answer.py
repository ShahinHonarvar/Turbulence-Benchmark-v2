from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            for anagram in anagram_dict:
                if is_anagram(anagram, s):
                    anagram_dict[anagram].append(s)
                    break
            else:
                anagram_dict[s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs >= 189