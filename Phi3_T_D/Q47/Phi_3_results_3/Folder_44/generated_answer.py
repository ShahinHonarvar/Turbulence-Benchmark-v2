def palindromes_of_specific_lengths(s):
    substr = s[18:99].lower()
    palindromes = set()
    for i in range(len(substr)):
        for length in range(31, 52):
            if i + length <= len(substr):
                candidate = substr[i:i + length]
                if candidate == candidate[::-1] and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes