def palindromes_of_specific_lengths(s):
    s = s[62:71].lower()
    palindromes = set()
    for i in range(len(s)):
        if 3 <= i <= len(s) - 4:
            for j in range(i + 3, i + 6):
                if s[i:j] == s[j:i:-1]:
                    palindromes.add(s[i:j])
        if 2 <= i <= len(s) - 5:
            if s[i:i + 4] == s[i:i + 4][::-1]:
                palindromes.add(s[i:i + 4])
    return {''.join(p) for p in palindromes if p.isalpha()}