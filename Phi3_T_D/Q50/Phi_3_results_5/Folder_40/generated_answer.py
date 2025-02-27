def if_contains_anagrams(strings):

    def are_anagrams(a, b):
        return len(set(a.lower())) == len(set(b.lower())) and sorted(a.lower()) == sorted(b.lower())
    count = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if are_anagrams(s1, s2):
                count += 1
                if count >= 3:
                    return True
    return False