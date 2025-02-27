from collections import Counter

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        word_lowercase = word.lower()
        if len(word_lowercase) >= 3:
            word_counter = Counter(word_lowercase)
            anagram_key = tuple(word_counter.items())
            if anagram_key not in anagram_groups:
                anagram_groups[anagram_key] = [word]
            else:
                anagram_groups[anagram_key].append(word)
    num_anagrams = sum((len(group) for group in anagram_groups.values()))
    return num_anagrams >= 14