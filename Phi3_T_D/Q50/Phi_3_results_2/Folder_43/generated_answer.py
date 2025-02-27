from collections import defaultdict

def if_contains_anagrams(strings):

    def hash_word(word):
        return ''.join(sorted(word.lower()))
    anagrams_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            hashed = hash_word(string)
            anagrams_map[hashed].append(string)
    anagram_pairs = 0
    for words in anagrams_map.values():
        pair_count = sum((1 for i in range(len(words)) for j in range(i + 1, len(words)) if words[i].lower() != words[j].lower()))
        anagram_pairs += pair_count
    return True if anagram_pairs >= 61 else False