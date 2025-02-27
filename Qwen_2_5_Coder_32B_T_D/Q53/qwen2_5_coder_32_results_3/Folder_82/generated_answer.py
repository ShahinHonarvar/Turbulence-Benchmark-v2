def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 72, n + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result