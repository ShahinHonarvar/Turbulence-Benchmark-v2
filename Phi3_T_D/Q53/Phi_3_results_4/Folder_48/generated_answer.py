def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s_lower)):
        for j in range(i + 149, len(s_lower)):
            substring = s_lower[i:j + 1]
            if substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes