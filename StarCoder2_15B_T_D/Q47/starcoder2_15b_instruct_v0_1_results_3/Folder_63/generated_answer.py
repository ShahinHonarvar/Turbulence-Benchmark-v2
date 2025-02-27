from typing import Set

def palindromes_of_specific_lengths(text: str) -> Set[str]:
    """
    Finds all palindromes of specific lengths in a given text.
    """
    subtext = text[33:86]
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(subtext) - length + 1):
            window = subtext[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes