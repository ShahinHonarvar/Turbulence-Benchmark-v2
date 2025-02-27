def if_contains_anagrams(lst):

    def get_char_count(s):
        return tuple(sorted(s.lower()))
    count = 0
    seen = {}
    for s in lst:
        if len(s) >= 3:
            char_count = get_char_count(s)
            if char_count in seen:
                seen[char_count] += 1
            else:
                seen[char_count] = 1
            if seen[char_count] > 1:
                count += seen[char_count] - 1
    return count >= 52