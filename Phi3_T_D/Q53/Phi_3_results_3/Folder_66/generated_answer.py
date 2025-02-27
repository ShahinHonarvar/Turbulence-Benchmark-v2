def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = 76
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    palindromes_76plus = {pal for pal in palindromes if len(pal) >= 76}
    return palindromes_76plus