import re
def sort_numbers_in_string(s):
    numbers = re.findall(r'\d+', s)
    numbers = [int(num) for num in numbers]
    numbers.sort()
    result = []
    number_idx = 0 
    i = 0
    while i < len(s):
        if s[i].isdigit():
            number = ''
            while i < len(s) and s[i].isdigit():
                number += s[i]
                i += 1
            result.append(str(numbers[number_idx]))
            number_idx += 1
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)
s =input().strip()
print(sort_numbers_in_string(s))
