def if_contains_anagrams(strings):
    count = 0
    normalized = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    unique_sorted_strings = set(normalized)
    for sorted_str in unique_sorted_strings:
        count += sum((1 for s in normalized if s == sorted_str))
        if count > 89:
            return False
    return True