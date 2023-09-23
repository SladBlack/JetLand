# Палиндром — это число, которое одинаково читается в обоих направлениях. Например, 123321 — это палиндром.
# Необходимо найти самый большой палиндром, равный произведению двух 3-значных чисел.

def is_palindrome(num: int) -> bool:
    """
    Check if number is palindrome
    :param num: int
    :return: bool
    """
    num_str = str(num)
    return num_str == num_str[::-1]


def biggest_palindrome() -> int:
    """
    Find the biggest palindrome equal to the product of two 3-digit numbers
    :return: int
    """
    max_num = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if is_palindrome(num) and num > max_num:
                max_num = num

    return max_num


if __name__ == '__main__':
    print(biggest_palindrome())
