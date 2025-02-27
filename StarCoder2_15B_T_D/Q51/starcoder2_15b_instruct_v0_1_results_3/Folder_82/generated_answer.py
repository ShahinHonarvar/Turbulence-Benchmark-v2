import re

def if_contains_anagrams(strings):
    canonical_forms = {}
    for string in strings:
        string = re.sub('[^a-z]', '', string.lower())
        if len(string) >= 3:
            canonical_form = ''.join(sorted(string))
            canonical_forms[canonical_form] = canonical_forms.get(canonical_form, 0) + 1
    anagram_count = 0
    for canonical_form, count in canonical_forms.items():
        if count > 1:
            anagram_count += count - 1
    return anagram_count <= 40