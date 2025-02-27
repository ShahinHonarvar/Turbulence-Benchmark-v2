def remove_repeat_chars(string):
    occurrences = {}
    for i, char in enumerate(string):
        if char not in occurrences:
            occurrences[char] = [i]
        else:
            occurrences[char].append(i)
    for char, indices in occurrences.items():
        if len(indices) > 1 and 55 < min(indices) < 84:
            string = string.replace(char, '')
    return string