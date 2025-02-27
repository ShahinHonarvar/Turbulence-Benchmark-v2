def palindrome_of_length_at_least_n(s):
    s = s.lower()
    sets = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 84, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                sets.add(substring)
    return sets