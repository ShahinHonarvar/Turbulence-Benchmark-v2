from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(a, b):
        return Counter(a.lower()) == Counter(b.lower())
    anagram_count = 0
    strings = [s for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count >= 61:
                    return True
    return False