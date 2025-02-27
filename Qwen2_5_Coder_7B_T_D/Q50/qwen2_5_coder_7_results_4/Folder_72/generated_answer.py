from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_count = 0
    words = [word for word in words if len(word) >= 3]
    word_set = set(words)
    for word in word_set:
        if word in words:
            for other_word in word_set:
                if other_word != word and is_anagram(word, other_word):
                    anagram_count += 1
    return anagram_count >= 55