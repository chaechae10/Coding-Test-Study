input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    result = []
    for i in range(2, number):
        if not (i % 2 == 0 or i % 3 == 0):
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)

## [2, 3, 5, 7, 11, 13, 17, 19]
