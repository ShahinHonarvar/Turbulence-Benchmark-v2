def palindromes_of_specific_lengths(s):
    s = s[13:100]
    results = set()
    for i in range(len(s) - 25):
        for j in range(i + 25, min(i + 29, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                results.add(substring)
    return results