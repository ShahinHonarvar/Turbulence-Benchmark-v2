from collections import defaultdict

def if_contains_anagrams(words):
    lengthy_anagrams = defaultdict(int)
    for word in words:
        key = ''.join(sorted(word.lower())).lstrip('-')
        if key and len(word) >= 3:
            lengthy_anagrams[key] += 1
    return sum((count >= 2 for count in lengthy_anagrams.values())) >= 11