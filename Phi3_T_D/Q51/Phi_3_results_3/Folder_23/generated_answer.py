from collections import Counter

def if_contains_anagrams(strings):

    def char_frequency(string):
        return Counter(''.join((char for char in string if char.isalpha())).lower())

    def are_anagrams(str1, str2):
        return char_frequency(str1) == char_frequency(str2)
    count = 0
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                sorted_pair = tuple(sorted((strings[i], strings[j])))
                if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted_pair not in anagram_pairs):
                    count += 1
                    anagram_pairs.add(sorted_pair)
                    if count > 49:
                        return False
    return True