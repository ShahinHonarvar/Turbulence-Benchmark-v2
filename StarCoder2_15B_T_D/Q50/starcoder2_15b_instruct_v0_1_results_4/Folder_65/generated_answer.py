def if_contains_anagrams(strings):
    anagram_pairs = 0
    compared_indices = set()
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and j not in compared_indices and is_anagram(string1, string2):
                anagram_pairs += 1
                compared_indices.add(i)
                compared_indices.add(j)
    return anagram_pairs >= 94

def is_anagram(string1, string2):
    if len(string1) >= 3 and len(string2) >= 3:
        sorted_string1 = sorted(string1.lower())
        sorted_string2 = sorted(string2.lower())
        return sorted_string1 == sorted_string2
    else:
        return False