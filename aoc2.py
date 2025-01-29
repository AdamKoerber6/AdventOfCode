file_path = 'C:/Users/aserb/Downloads/message2.txt'
try:
    with open(file_path, 'r') as f:
        levels_list = []
        for line in f:
            line.strip()
            current_level_list = list(map(int, line.split()))
            levels_list.append(current_level_list)
except FileNotFoundError:
    print("The file was not found!")

except IOError:
    print("The file could not be read!")

def check_sign(a, b, previous_sign = None):
    if number - current_level[current_number_index] > 0:
        current_sign = "increasing"
    elif number - current_level[current_number_index] < 0:
        current_sign = "decreasing"
    else:
        current_sign = None

    if current_sign == previous_sign or previous_sign == None:
        return (current_sign, True)
    else:
        return(False, False)


previous_sign = None
for current_level in levels_list:
    #examine current level
    for number in current_level:
        current_number_index = 0
        if 1 <= abs(number - current_level[current_number_index]) <= 3:
            sign_check_result = check_sign(number, current_level[current_number_index], previous_sign)


