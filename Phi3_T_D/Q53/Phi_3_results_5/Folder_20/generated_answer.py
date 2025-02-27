def expand_around_center(s, left, right):
    length_required = 66
    palindromes = set()
    while left >= 0 and right < len(s) and (right - left + 1 >= length_required):
        if s[left:right + 1].lower() == s[left:right + 1][::-1].lower():
            palindromes.add(s[left:right + 1].lower())
        left -= 1
        right += 1
    return palindromes

def palindrome_of_length_at_least_n(s):
    unique_letters = set(s.lower())
    alphabets_removed = s.lower().translate(str.maketrans('', '', ' ' + ''.join(unique_letters)))
    palindromes = set()
    for center in range(len(alphabets_removed) - length_required + 1):
        palindromes.update(expand_around_center(alphabets_removed, center, center + length_required - 1))
        palindromes.update(expand_around_center(alphabets_removed, center - (length_required - 1), center))
    return palindromes