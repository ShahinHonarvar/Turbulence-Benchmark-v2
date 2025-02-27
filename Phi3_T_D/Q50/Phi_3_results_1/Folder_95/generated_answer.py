from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            sorted_anagrams[sorted_word].append(word)
    anagram_pairs = 0
    seen = set()
    for anagrams in sorted_anagrams.values():
        for word in anagrams:
            if word not in seen:
                seen.add(word)
                pair_count = sum((1 for other_word in anagrams if other_word != word))
                anagram_pairs += pair_count
    return anagram_pairs >= 93