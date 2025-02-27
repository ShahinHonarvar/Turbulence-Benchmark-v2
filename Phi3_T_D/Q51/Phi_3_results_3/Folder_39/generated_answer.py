from collections import defaultdict

def if_contains_anagrams(lst):

    def clean_and_sort(s):
        return ''.join(sorted(filter(str.isalpha, s.lower()))).lstrip()
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    anagram_counts = defaultdict(int)
    for word in sorted_words:
        anagram_counts[word] += 1
    return sum((1 for count in anagram_counts.values() if count > 1)) <= 257