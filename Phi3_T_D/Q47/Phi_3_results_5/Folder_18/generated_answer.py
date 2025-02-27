def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    palindromes = set()
    for center in range(len(s)):
        for radius in range(1, min((len(s) - center) // 2, 54) + 1):
            left, right = (center - radius, center + radius)
            if left >= 0 and right < len(s) and (s[left] == s[right]):
                if all((c.isalpha() for c in s[left:right + 1])):
                    palindromes.add(s[left:right + 1].capitalize())
    return {p for p in palindromes if 13 <= len(p) <= 66}