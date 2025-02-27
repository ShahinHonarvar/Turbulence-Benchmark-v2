def if_contains_anagrams(strings_list):
    count = 0
    strings_list = [(s.lower(), ''.join(sorted(s.lower()))) for s in strings_list]
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            if len(strings_list[i][0]) >= 3 and len(strings_list[j][0]) >= 3 and (strings_list[i][1] == strings_list[j][1]):
                count += 1
    return count >= 144