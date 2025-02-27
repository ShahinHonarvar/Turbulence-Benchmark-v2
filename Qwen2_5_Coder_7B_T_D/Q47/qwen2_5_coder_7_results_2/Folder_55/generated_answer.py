def palindromes_of_specific_lengths(s):
    substr = s[10:76]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 10, min(len(substr), i + 21)):
            sub = substr[i:j]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes