def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        canonical_form = ''.join(sorted(word.lower()))
        if len(canonical_form) >= 3 and canonical_form.isalpha():
            anagrams[canonical_form] = anagrams.get(canonical_form, 0) + 1
    return len(anagrams) <= 474