def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def extract_letters(subs):
        return ''.join(filter(str.isalpha, subs)).lower()
    s_sub = s[119:257]
    cleaned_sub = extract_letters(s_sub)
    palindromes = set()
    for length in range(104, 124):
        for i in range(len(cleaned_sub) - length + 1):
            part = cleaned_sub[i:i + length]
            if is_palindrome(part):
                palindromes.add(part)
    return palindromes