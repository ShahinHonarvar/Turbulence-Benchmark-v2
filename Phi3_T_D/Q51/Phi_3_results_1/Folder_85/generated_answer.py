from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return len(w1) >= 3 and len(w2) >= 3 and (Counter(w1.lower()) == Counter(w2.lower()))
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                count += 1
                if count > 276:
                    return False
    return True