def palindromes_of_specific_lengths(s):
    substring = s[16:61]
    results = set()
    for i in range(len(substring)):
        for j in range(i + 16, i + 40):
            if j > len(substring):
                break
            candidate = substring[i:j + 1]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                results.add(candidate)
    return results