from collections import defaultdict

def if_contains_anagrams(strings):

    def process_string(s):
        return ''.join(sorted(s.lower())).lstrip('a') or None
    anagrams_dict = defaultdict(int)
    for string in strings:
        anagram = process_string(string)
        if anagram:
            anagrams_dict[anagram] += 1
    count_anagrams = 0
    for anagram, frequency in anagrams_dict.items():
        if len(anagram) >= 3:
            count_anagrams += frequency * (frequency - 1) // 2
    return count_anagrams >= 36