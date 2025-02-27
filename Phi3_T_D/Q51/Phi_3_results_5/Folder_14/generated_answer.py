from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        count = defaultdict(int)
        for char in s.lower():
            if char.isalpha():
                count[char] += 1
        return tuple(sorted(count.items()))
    seen_anagrams = defaultdict(int)
    for string in strings:
        letters = count_letters(string)
        if len(string) >= 3:
            seen_anagrams[letters] += 1
    return sum((count * (count - 1) // 2 for count in seen_anagrams.values())) <= 474