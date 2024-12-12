from day_3 import extract_and_multiply

def test_example_memory():
    test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = extract_and_multiply(test)
    assert result == 161
