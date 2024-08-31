line_size = 100
total_line = 0
line_over_range = 0
total_over_char = 0
print("line_size : ", line_size)
print()

try:
    with open('./Homework/what_is_python.txt', 'r',encoding='utf-8') as f:
        contents = f.readlines()
        total_line = contents.__len__()
        i = 1
        for line in contents:
            if line.__len__() > line_size:
                n_over_char = line.__len__() - line_size
                total_over_char = total_over_char + n_over_char
                line_over_range = line_over_range + 1
                print("line", i, "more than specified,", n_over_char, "characters")
            i = i + 1
except Exception as e:
    print(f"error is {e}        {e.__class__}")

print('\ntotal line :', total_line, 'lines')
print('number line over range :', line_over_range, 'lines')
print('total over character :', total_over_char, 'characters')