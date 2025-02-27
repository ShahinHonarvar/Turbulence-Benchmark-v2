def if_contains_anagrams(words):
    all_sorted = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_count = 0
    for word in all_sorted:
        anagram_count += all_sorted.count(word) > 1
    return anagram_count >= 66