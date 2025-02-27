def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 33
    palindromes = set()
    for i in range(len(s) - n + 1):
        word = s[i:i + n]
        if word == word[::-1] and word.isalpha():
            palindromes.add(word)
    return palindromes