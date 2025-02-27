def if_contains_anagrams(strings):
    lowered_strings = [''.join(sorted(s.lower())) for s in strings]
    hash_map = {}
    anagrams_count = 0
    for string in lowered_strings:
        if len(string) >= 3:
            if string in hash_map:
                anagrams_count += hash_map[string]
                hash_map[string] += 1
            else:
                hash_map[string] = 1
    return anagrams_count <= 79