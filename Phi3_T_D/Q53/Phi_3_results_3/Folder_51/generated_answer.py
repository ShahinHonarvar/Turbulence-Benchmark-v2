def palindrome_of_length_at_least_n(s):
    length = len(s)
    result = set()
    palindrome = lambda x: x == x[::-1]
    s_low = s.lower()
    for i in range(length):
        for j in range(i + 63, length + 1):
            substr = s_low[i:j]
            if palindrome(substr):
                result.add(substr)
    return result