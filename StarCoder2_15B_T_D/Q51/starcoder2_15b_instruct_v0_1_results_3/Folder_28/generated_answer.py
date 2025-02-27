def if_contains_anagrams(strings):
    sorted_forms = [''.join(sorted(string.lower())) for string in strings if len(string) >= 3 and all((c.isalpha() for c in string.lower()))]
    sorted_form_to_indices = {}
    for i, sorted_form in enumerate(sorted_forms):
        if sorted_form not in sorted_form_to_indices:
            sorted_form_to_indices[sorted_form] = [i]
        else:
            sorted_form_to_indices[sorted_form].append(i)
    anagram_pairs = 0
    for sorted_form, indices in sorted_form_to_indices.items():
        if len(indices) >= 2:
            anagram_pairs += len(indices) * (len(indices) - 1) // 2
    return anagram_pairs <= 78