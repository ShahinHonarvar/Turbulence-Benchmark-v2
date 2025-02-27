def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 41
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + n, length + 1):
            word = s[start:end]
            if word == word[::-1] and word.isalpha():
                result.add(word)
    return result