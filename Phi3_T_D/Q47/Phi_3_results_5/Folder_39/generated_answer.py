def palindromes_of_specific_lengths(s):

    def find_palindromes(sub_s):
        palindromes = set()
        for length in range(50, 54):
            for i in range(len(sub_s) - length + 1):
                word = sub_s[i:i + length]
                if word.isalpha() and word.lower() == word[::-1].lower():
                    palindromes.add(word)
        return palindromes
    if len(s) < 92:
        return set()
    sub_s = s[31:92]
    return find_palindromes(sub_s)