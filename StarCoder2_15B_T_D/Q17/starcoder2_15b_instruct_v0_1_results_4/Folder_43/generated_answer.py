def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums:
        if num % -77 == 0 and num % -32 == 0:
            result.append(num)
    return result

def test_all_ints_div_by_both_two_nums():
    nums = [i for i in range(-100, 100)]
    expected = [-560, -280, -140, -70, -44, -22, 0, 22, 44, 70, 140, 280]
    actual = all_ints_div_by_both_two_nums(nums)
    assert actual == expected