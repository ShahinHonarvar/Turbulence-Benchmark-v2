import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    length_range = range(3, 6)
    substring = string[:10]
    pattern = re.compile('[a-zA-Z]+')
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if j - i + 1 in length_range:
                substring_to_check = substring[i:j + 1]
                if pattern.match(substring_to_check) and substring_to_check.lower() == substring_to_check[::-1].lower():
                    palindromes.add(substring_to_check)
    return palindromes