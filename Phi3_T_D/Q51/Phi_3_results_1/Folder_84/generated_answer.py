def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    count = 0
    normalized_strings = {normalize(s): [] for s in strings}
    for string in strings:
        normalized_strings[normalize(string)].append(string)
    for key in normalized_strings:
        if len(normalized_strings[key]) > 1:
            pairs = sum((1 for i in range(len(normalized_strings[key])) for j in range(i + 1, len(normalized_strings[key])) if sorted(normalized_strings[key][i]) == sorted(normalized_strings[key][j])))
            count += pairs
    return count <= 16