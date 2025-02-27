from collections import defaultdict

def if_contains_anagrams(lst):

    def count_letters(word):
        count = defaultdict(int)
        for char in word.lower():
            if char.isalpha():
                count[char] += 1
        return count
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(count_letters(word).items()))].append(word)
    pairs = sum((len(a) for a in anagrams.values())) // 2
    return pairs <= 92