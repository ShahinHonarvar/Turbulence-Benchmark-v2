from collections import defaultdict

def if_contains_anagrams(lst):

    def count_letters(word):
        return ''.join(sorted(word.lower()))

    def meets_conditions(word):
        return len(word) >= 3 and word.isalpha()
    anagram_groups = defaultdict(list)
    for word in lst:
        if meets_conditions(word):
            anagram_groups[count_letters(word)].append(word)
    count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            count += sum(range(len(group)))
    return count <= 57