def add_digits(num):
    def sum_of(num):
        temp = 0
        for i in str(num):
            temp += int(i)
        return temp
    output = sum_of(num)
    while output >= 10:
        if output >= 10:
            output = sum_of(output)
    return output





