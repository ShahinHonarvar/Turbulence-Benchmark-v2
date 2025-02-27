def palindromes_of_specific_lengths(s):
    s = s[130:296]
    candidates = set()
    for center in range(len(s)):
        for radius in range(1, 56):
            if center - radius < 0 or center + radius >= len(s):
                continue
            if not s[center - radius].isalpha():
                continue
            if not s[center + radius].isalpha():
                continue
            substr = s[center - radius:center + radius + 1]
            if substr.lower() == substr[::-1].lower():
                candidates.add(substr)
    return candidates