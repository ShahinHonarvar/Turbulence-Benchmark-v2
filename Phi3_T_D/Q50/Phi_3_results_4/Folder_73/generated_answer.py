def if_contains_anagrams(lst):
    filtered_lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    anagram_set = {item for item in filtered_lst if filtered_lst.count(item) > 1}
    return len(anagram_set) >= 91