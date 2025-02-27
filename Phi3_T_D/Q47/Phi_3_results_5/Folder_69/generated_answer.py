def palindromes_of_specific_lengths(s):
    candidate = s[11:97]
    results = set()
    for length in range(45, 53):
        for i in range(len(candidate) - length + 1):
            substring = candidate[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                results.add(substring.lower())
    return results