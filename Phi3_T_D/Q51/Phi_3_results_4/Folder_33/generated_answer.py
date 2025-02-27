def if_contains_anagrams(lst):
    pairs_count = 0
    seen = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen:
            pairs_count += seen[sorted_word]
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
    return pairs_count <= 85