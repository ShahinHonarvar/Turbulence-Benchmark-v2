from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return Counter(w1) == Counter(w2)
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (words[i].lower() != words[j].lower()) and is_anagram(words[i].lower(), words[j].lower()):
                anagram_pairs += 1
                if anagram_pairs > 46:
                    return False
    return True