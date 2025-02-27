def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    target_length = 366
    for i in range(len(s) - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes