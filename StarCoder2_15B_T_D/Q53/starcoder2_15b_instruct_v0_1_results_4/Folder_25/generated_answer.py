def palindrome_of_length_at_least_n(s):
    processed_string = ''.join((c for c in s.lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(processed_string) - 37):
        substring = processed_string[i:i + 38]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes