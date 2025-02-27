def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3 and canonical_form.isalpha():
            if canonical_form in anagrams:
                anagrams[canonical_form] += 1
            else:
                anagrams[canonical_form] = 1
    return len(anagrams) <= 52