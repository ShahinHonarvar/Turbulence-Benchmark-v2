def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 147
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n - 1, length):
            substr = s[i:j + 1]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result