def palindrome_of_length_n(s):
    set_of_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 209):
        substring = s[i:i + 210]
        if substring == substring[::-1]:
            set_of_palindromes.add(substring)
    return set_of_palindromes