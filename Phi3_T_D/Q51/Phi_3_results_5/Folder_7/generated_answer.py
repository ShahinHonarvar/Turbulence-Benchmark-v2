def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    seen = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        norm_string = normalize(string)
        seen[norm_string] = seen.get(norm_string, 0) + 1
        count += seen[norm_string] - 1
        if count >= 445:
            return False
    return True