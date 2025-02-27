def palindromes_of_specific_lengths(s: str) -> set:
    s = s[1:9].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 5, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result