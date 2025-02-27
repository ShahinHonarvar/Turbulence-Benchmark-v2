def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[125:284]
    for i in range(len(substring)):
        for j in range(i + 109, min(i + 127, len(substring) + 1)):
            sub = substring[i:j]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                result.add(sub)
    return result