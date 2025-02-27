def palindrome_of_length_n(s):
    pset = set()
    length = 10
    s = s.lower()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            pset.add(substr)
    return pset