def if_contains_anagrams(strings):
    str_set = set()
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in str_set:
                return True
            str_set.add(sorted_string)
    return False