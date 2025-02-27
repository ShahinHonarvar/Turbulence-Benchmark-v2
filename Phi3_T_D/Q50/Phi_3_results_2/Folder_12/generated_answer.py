from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagram_dict[key].append(string)
    for key, values in anagram_dict.items():
        anagram_count += sum((1 for i, s1 in enumerate(values) for s2 in values[i + 1:] if are_anagrams(s1, s2)))
    return anagram_count >= 69