def palindromes_of_specific_lengths(s):
    start, end = (15, 86)
    s = s.lower()
    half_length = (end - start + 1) // 2
    palindromes = set()
    for i in range(start, start + half_length - 2):
        if not s[i].isalpha():
            continue
        for j in range(half_length, min(i + 10, end - start + 1)):
            if not s[i + j - half_length].isalpha():
                continue
            substr = s[i:i + j]
            substr_rev = substr[::-1]
            if substr == substr_rev:
                palindromes.add(substr.upper())
    return palindromes if 51 <= len(palindromes.pop()) <= 60 else set()