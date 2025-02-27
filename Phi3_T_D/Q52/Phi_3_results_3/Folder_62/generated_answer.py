def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    len_s = len(s)
    for i in range(len_s - 187):
        substring = s[i:i + 188]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes