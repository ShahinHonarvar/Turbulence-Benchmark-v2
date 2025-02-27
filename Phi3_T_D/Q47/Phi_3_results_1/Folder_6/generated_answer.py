def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[45:99]
    for length in range(40, 48):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                if candidate.isalpha():
                    result.add(candidate.lower())
    return result