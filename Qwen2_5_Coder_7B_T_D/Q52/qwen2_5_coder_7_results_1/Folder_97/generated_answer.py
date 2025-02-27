def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 209):
        substring = s[i:i + 210]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes