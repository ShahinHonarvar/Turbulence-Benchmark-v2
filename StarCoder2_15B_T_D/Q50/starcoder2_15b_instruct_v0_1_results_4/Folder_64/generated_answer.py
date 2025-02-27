def if_contains_anagrams(strings):
    filtered_strings = [string for string in strings if len(string) >= 3]
    lowercase_strings = [string.lower() for string in filtered_strings]
    sorted_strings = [sorted(string) for string in lowercase_strings]
    sorted_string_counts = {}
    for sorted_string in sorted_strings:
        if ''.join(sorted_string) in sorted_string_counts:
            sorted_string_counts[''.join(sorted_string)].append(sorted_string)
        else:
            sorted_string_counts[''.join(sorted_string)] = [sorted_string]
    return any((len(counts) >= 5 for counts in sorted_string_counts.values()))