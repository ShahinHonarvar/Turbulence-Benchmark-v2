def palindromes_of_specific_lengths(s):
    result = set()
    s = s[45:99].lower()
    for i in range(len(s)):
        for j in range(i + 40, min(i + 48, len(s)) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result