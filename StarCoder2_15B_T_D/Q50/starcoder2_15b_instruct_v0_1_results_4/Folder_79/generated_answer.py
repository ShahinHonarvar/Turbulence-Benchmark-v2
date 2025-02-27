def if_contains_anagrams(input_list):
    anagrams = {}
    for word in input_list:
        canonical_form = ''.join(sorted(word.lower()))
        if canonical_form in anagrams:
            anagrams[canonical_form].append(word)
        else:
            anagrams[canonical_form] = [word]
    return len([pairs for pairs in anagrams.values() if len(pairs) >= 3]) >= 40