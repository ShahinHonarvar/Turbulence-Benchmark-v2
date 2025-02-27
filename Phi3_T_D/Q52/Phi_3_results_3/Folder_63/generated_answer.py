def palindrome_of_length_n(s):
    s = s.lower()
    palindromes_set = set()
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if substring == substring[::-1]:
            palindromes_set.add(substring.upper())
    return palindromes_set