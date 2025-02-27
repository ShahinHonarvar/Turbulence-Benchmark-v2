def if_contains_anagrams(strings):
    pairs = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                pairs += 1
                if pairs >= 81:
                    return True
    return False