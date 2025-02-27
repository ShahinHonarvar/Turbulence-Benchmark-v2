def all_substring_of_size_n(text):
    substring_set = set()
    for i in range(len(text) - 17):
        substring = text[i:i + 18]
        if len(set(substring)) == 18:
            substring_set.add(substring)
    return list(substring_set)