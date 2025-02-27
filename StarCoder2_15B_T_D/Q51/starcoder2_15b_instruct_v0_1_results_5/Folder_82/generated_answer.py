def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3 and canonical_form.isalpha():
            if canonical_form in anagrams:
                anagrams[canonical_form] += 1
            else:
                anagrams[canonical_form] = 1
    return len([freq for freq in anagrams.values() if freq >= 2]) <= 40