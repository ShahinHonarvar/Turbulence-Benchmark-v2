def if_contains_anagrams(strings):

    def canonize(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    seen = set()
    for string in strings:
        if len(string) < 3:
            continue
        canonized_string = canonize(string)
        if canonized_string in seen:
            anagrams_count += 1
        else:
            seen.add(canonized_string)
        if anagrams_count > 59:
            return False
    return True