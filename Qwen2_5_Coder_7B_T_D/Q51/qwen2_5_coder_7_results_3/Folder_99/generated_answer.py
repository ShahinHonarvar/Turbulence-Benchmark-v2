from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    word_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            word_map[''.join(sorted(word.lower()))].append(word)
    for group in word_map.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if is_anagram(group[i], group[j]):
                        anagram_pairs += 1
                        if anagram_pairs > 93:
                            return False
    return True