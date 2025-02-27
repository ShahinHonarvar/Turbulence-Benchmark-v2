def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(31):
        for j in range(i + 20, i + 31):
            if s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j].lower()
                if all((c.isalpha() for c in palindrome)):
                    palindromes.add(palindrome)
    return palindromes