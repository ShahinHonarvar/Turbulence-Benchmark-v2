def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 59
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            word = s[i:j]
            if word == word[::-1] and word.isalpha():
                result.add(word)
    return result