def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return sorted(w1.lower()) == sorted(w2.lower())
    anagram_pairs = 0
    words = [word for word in words if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 18:
                    return False
    return True