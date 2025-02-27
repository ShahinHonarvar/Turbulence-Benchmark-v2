def palindrome_of_length_at_least_n(s):
    set_of_palindromes = set()
    s = s.lower()
    for i, char in enumerate(s):
        for length in range(28, len(s) - i + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes