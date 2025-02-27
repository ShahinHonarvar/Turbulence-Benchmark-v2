def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[40:95].lower()
    for i in range(45, 52):
        for j in range(len(substring) - i + 1):
            candidate = substring[j:j + i]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result