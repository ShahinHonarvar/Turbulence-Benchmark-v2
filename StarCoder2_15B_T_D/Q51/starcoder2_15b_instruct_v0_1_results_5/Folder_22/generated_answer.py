def if_contains_anagrams(strings):
    filtered_strings = [s for s in strings if len(s) >= 3]
    anagram_pairs = set()
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if sorted(filtered_strings[i].lower()) == sorted(filtered_strings[j].lower()):
                anagram_pairs.add((filtered_strings[i], filtered_strings[j]))
    return len(anagram_pairs) <= 14