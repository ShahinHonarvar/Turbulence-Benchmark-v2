from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        counter1, counter2 = (Counter(str1.lower()), Counter(str2.lower()))
        return counter1 == counter2 and len(str1) >= 3 and (len(str2) >= 3)
    anagram_pairs = [(strings[i], strings[j]) for i in range(len(strings)) for j in range(i + 1, len(strings)) if is_anagram(strings[i], strings[j])]
    return len(anagram_pairs) <= 147