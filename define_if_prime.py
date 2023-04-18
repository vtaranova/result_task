def is_prime(num):
    div = 0
    div_count = 0
    if num > 1:
        while div < num + 1:
            if num % div == 0:
                div_count += 1
            div += 1
    else:
        return False
    if div_count > 2:
        return False
    else:
        return True

