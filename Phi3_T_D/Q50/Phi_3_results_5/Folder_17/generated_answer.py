from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    len_of_three_or_more = (word for word in strings if len(word) >= 3)
    sorted_anagrams = defaultdict(list)
    for word in len_of_three_or_more:
        sorted_anagrams[''.join(sorted(word.lower()))].append(word)
    count = 0
    for anagram_group in sorted_anagrams.values():
        if len(anagram_group) > 1:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count >= 97