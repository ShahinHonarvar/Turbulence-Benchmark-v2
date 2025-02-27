def if_contains_anagrams(strings):

    def clean_and_sort(s):
        return ''.join(sorted(s.lower()))
    clean_strings = [clean_and_sort(s) for s in strings]
    seen = set()
    count = 0
    for cs in clean_strings:
        if cs in seen:
            count += 1
        if count > 20:
            return False
        seen.add(cs)
    return True