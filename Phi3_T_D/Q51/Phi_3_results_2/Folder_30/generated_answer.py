from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        return sorted(s.lower())
    letter_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            used_counts = count_letters(string)
            letter_counts[used_counts] += 1
    anagram_pairs = 0
    for count in letter_counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 28