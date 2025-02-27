from collections import Counter

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    letter_counts = Counter(substring)
    palindromes = set()
    for letter, count in letter_counts.items():
        if count >= 2:
            middle_letter = [let for let, cnt in letter_counts.items() if cnt % 2 != 0]
            if not middle_letter:
                middle_letter = ''
            else:
                middle_letter = middle_letter[0]
            palindrome = letter + middle_letter + letter
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes