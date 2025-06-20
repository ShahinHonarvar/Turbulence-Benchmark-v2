from Q47.starcoder2_15B_results_2.Folder_81.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(122, 220)
    m = min(122 - 12 + 1, 220)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(12, m + 1)}


def test_string_of_similar_nums():
    n = max(122, 220)
    m = min(122 - 12 - 1, 220)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (122 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (122 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (122 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(122 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 12 <= len(i) <= 220


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(122 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[12: 122 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (122 * 3)
    assert not palindromes_of_specific_lengths(s)
    