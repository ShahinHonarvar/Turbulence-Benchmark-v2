from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams_of_three_letters(str1, str2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1.lower()) == sorted(str2.lower())):
            return True
        return False
    anagram_pairs = 0
    anagram_map = defaultdict(int)
    for word in strings:
        key = ''.join(sorted(word.lower()))
        anagram_map[key] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 59