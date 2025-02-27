def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 74, n + 1):
            word = s[i:j]
            if word.isalpha() and word == word[::-1]:
                result_set.add(word)
    return result_set