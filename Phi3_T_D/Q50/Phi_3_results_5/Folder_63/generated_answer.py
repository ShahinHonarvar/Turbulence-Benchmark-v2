def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    string_dict = {}
    for s in strings:
        if len(s) >= 3:
            key = normalize(s)
            if key in string_dict:
                count += string_dict[key]
                string_dict[key] += 1
            else:
                string_dict[key] = 1
    return count >= 89