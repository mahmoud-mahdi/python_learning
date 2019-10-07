"""It is dealing only with one fixed hard coded value
    without any validation but we can add more functionality
    like getting the input interactively from the user
    and also we can add some validation that the number
    is positive"""


def get_results(number):
    result = []
    result.append(number)
    while result[-1] != 1:
        if result[-1] % 2 == 0:
            result.append(int(result[-1] / 2))
        else:
            result.append((result[-1] * 3) + 1)

    return result

# Those commented steps are to prent the sequence output for some number if needed

#number = 7
#final_result = get_results(number)
#final_length = len(final_result)
#print(', '.join(str(i) for i in final_result))
#print('The length of sequence of ' + str(number) + ' is: ' + str(final_length))


required_length = 0
for number in range(1, 10000000):
    final_result = get_results(number)
    final_length = len(final_result)
    if final_length > required_length:
        required_length = final_length
        required_number = number


print('The required number is: ', required_number)
print('The required sequence is: ',  required_length)
