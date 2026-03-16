def twice_trice(number):
    result1 = 2 * number
    result2 = 3 * number 
    return result1, result2

num = 5
twice, trice = twice_trice(num)  # multiple assignment
multiples = twice_trice(num)  # multiples contains both values (tuple)

