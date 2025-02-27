from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    anagram_pairs = sum((choose(len(v), 2) for v in word_dict.values() if len(v) > 1))
    return anagram_pairs >= 43