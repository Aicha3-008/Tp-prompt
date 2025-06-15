def calculate_average(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    average = total / len(numbers_list)
    return average

my_nums = [1, 2, 'three', 4]  
avg = calculate_average(my_nums)
print(f"Average: {avg}")
