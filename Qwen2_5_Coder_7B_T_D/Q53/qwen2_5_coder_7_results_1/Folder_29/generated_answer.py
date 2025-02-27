def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 78
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            word = s[i:j]
            if word == word[::-1] and word.isalpha():
                result.add(word)
    return result