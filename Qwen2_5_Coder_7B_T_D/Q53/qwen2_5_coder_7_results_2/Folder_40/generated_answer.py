def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 3, length + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                n_set.add(sub)
    return n_set