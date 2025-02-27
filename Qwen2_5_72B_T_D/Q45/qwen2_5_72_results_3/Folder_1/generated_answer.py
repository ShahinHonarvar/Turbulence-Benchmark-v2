from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:8]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    palindrome_components = {letter for letter, count in letter_counts.items() if count > 1}
    result_set = set()
    for first in palindrome_components:
        for second in palindrome_components:
            if letter_counts[first] > 1 and letter_counts[second] > (first == second):
                palindrome = first + second + second + first
                result_set.add(palindrome)
                if letter_counts[second] > 2:
                    palindrome = first + second * 2 + first
                    result_set.add(palindrome)
    return result_set