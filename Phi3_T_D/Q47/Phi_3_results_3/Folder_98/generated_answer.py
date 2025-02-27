def palindromes_of_specific_lengths(s):
    s = s[:21].lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(5, 81):
            if i + length > len(s):
                break
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes