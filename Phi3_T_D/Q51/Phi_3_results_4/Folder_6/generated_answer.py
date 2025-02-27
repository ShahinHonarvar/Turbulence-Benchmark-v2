from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        count = defaultdict(int)
        for char in s.lower():
            if char.isalpha():
                count[char] += 1
        return tuple(sorted(count.items()))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_counts[count_letters(string)] += 1
    num_anagrams = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return num_anagrams <= 86