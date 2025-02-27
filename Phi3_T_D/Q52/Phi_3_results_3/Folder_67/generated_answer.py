def palindrome_of_length_n(s):
    s_upper = s.upper()
    palindromes = set()
    for i in range(len(s_upper) - 41):
        substring = s_upper[i:i + 42]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes