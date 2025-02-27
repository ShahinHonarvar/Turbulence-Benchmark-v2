def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    palindromes = set()
    for i in range(len(s) - 49):
        substring = s[i:i + 51]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes