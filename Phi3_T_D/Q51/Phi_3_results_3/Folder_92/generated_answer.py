def if_contains_anagrams(strings):

    def first_n(s, n):
        return ''.join(sorted(s))[:n]

    def is_anagram(a, b):
        return first_n(a.lower(), len(a)) == first_n(b.lower(), len(b))
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 34:
                    return False
    return True