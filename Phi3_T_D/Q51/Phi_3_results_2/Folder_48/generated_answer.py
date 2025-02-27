def if_contains_anagrams(strings):

    def get_sorted_tuple(s):
        return tuple(sorted((char.lower() for char in s if char.isalpha())))
    count = 0
    seen = set()
    for s in strings:
        sorted_tuple = get_sorted_tuple(s)
        if sorted_tuple in seen:
            count += 1
        elif len(sorted_tuple) >= 3:
            seen.add(sorted_tuple)
    return count <= 277