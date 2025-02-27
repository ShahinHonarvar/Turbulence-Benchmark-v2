def is_palindrome_clean(s):
    i, j = (0, len(s) - 1)
    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

def palindromes_of_specific_lengths(text):
    subtext = text[13:99]
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(subtext) - length + 1):
            candidate = subtext[i:i + length]
            if is_palindrome_clean(candidate):
                palindromes.add(candidate.lower())
    return palindromes