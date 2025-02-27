def if_contains_anagrams(strings_list):

    def count_chars(word):
        return sorted(word.lower())
    counts = {}
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = count_chars(string)
            counts[sorted_string] = counts.get(sorted_string, 0) + 1
    pairs = sum((count // 2 for count in counts.values()))
    return pairs >= 88