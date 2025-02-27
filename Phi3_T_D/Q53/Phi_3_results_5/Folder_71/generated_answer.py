def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 87, len(s) + 1):
            substr = s[i:j]
            if not set(substr).difference('abcdefghijklmnopqrstuvwxyz'):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes