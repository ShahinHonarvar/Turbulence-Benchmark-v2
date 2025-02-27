from collections import defaultdict

def if_contains_anagrams(strings):
    length3_or_more = [s.lower() for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for word in length3_or_more:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for key in anagram_dict:
        words = anagram_dict[key]
        anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs >= 95