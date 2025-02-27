import re

def palindromes_of_specific_lengths(s):
    s = s[11:98].lower()
    regex = re.compile('[a-z]+')
    words = regex.findall(s)
    palindromes = set()
    for i in range(len(words)):
        for j in range(i, len(words)):
            subword = ''.join(words[i:j + 1])
            if 29 <= len(subword) <= 62 and subword == subword[::-1]:
                palindromes.add(subword)
    return palindromes