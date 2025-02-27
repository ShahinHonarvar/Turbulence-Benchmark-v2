def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    result = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(i + 6, len(s)) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result