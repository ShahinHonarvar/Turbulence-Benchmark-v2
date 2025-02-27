from collections import defaultdict

def if_contains_anagrams(string_list):

    def count_letters(s):
        return ''.join(sorted(s.lower()))

    def has_three_or_more_characters(s):
        return len(s) >= 3
    anagram_counts = defaultdict(int)
    for s in string_list:
        if has_three_or_more_characters(s):
            count = count_letters(s)
            anagram_counts[count] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 48