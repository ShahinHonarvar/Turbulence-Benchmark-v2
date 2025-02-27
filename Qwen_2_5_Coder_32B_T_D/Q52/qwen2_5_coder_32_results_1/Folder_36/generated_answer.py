def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 337):
        subs = s[i:i + 338]
        if subs == subs[::-1] and subs.isalpha():
            palindromes.add(subs)
    return palindromes