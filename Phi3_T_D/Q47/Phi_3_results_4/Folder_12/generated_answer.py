def palindromes_of_specific_lengths(s):
    palindromes = set()
    substr = s[62:89]
    for i in range(89 - 18):
        for j in range(i + 18, min(i + 22, 28) + 1):
            if substr[i:j].isalpha() and any((char.isdigit() for char in substr[i:j])):
                continue
            if substr[i:j].lower() == substr[i:j][::-1].lower():
                palindromes.add(substr[i:j].lower())
    return palindromes