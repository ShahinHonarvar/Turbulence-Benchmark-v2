def remove_repeat_chars(string):
    occurrences = {}
    for i, char in enumerate(string):
        if char not in occurrences:
            occurrences[char] = [i]
        else:
            occurrences[char].append(i)
    for char, indices in occurrences.items():
        if len(indices) > 1 and all((56 < index < 90 for index in indices)):
            string = string.replace(char, '')
    return string