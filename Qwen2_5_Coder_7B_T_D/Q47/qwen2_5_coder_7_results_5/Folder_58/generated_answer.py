def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[125:284]
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result