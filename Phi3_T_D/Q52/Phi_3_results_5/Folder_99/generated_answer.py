def palindrome_of_length_n(s):
    reduced_s = s.lower()
    palindromes = set()
    n = 420
    for i in range(len(reduced_s) - n + 1):
        substring = reduced_s[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring.capitalize())
    return palindromes