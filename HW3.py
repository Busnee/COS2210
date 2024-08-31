import threading

# -----------HW1--------------
line_size = 100
total_line = 0
line_over_range = 0
total_over_char = 0

def HW1(name, contents):
    global line_size, total_line, line_over_range, total_over_char
    print(f"task {name} start")
    # print(f"line_size : {line_size}")
    total_line = contents.__len__()
    i = 1
    for line in contents:
        if line.__len__() > line_size:
            n_over_char = line.__len__() - line_size
            total_over_char = total_over_char + n_over_char
            line_over_range = line_over_range + 1
            print(f"line {i} more than specified {n_over_char}, characters")
        i = i + 1
    print(f"task {name} finish")

# -----------HW2--------------
n_word_dict = { 'Python' : 0,
               'development' : 0,
               'software' : 0,
               'different' : 0}
reverse_dict = {'Python' : 'nohtyP',
               'development' : 'tnempoleved',
               'software' : 'erawtfos',
               'different' : 'tnereffid'}
new_contents = []

def reverse_word(word):
    for w in n_word_dict:
        if word == w:
            print(f"{w}+1")
            n_word_dict[w] = n_word_dict[w] + 1
            return reverse_dict[w]
    return word

def HW2(name, contents):
    global n_word_dict, reverse_dict, new_contents
    print(f"task {name} strat")
    for line in contents:
        word = line.strip().split()
        new_word = []
        for w in word:
            new_word.append(reverse_word(w))
        new_contents.append(new_word)
    print(f"task {name} finish")

# -----------HW3--------------
def main():
    try:
        with open('./Homework/what_is_python.txt', 'r',encoding='utf-8') as f:
            contents = f.readlines()
    except Exception as e:
        print(f"error is {e}        {e.__class__}")

    thread1 = threading.Thread(target=HW1, args=("HW1", contents,))
    thread2 = threading.Thread(target=HW2, args=("HW2", contents))

    # thread1.start()
    try:
        thread2.start()
        thread1.start()
    except Exception as e:
        print(f"error is {e}        {e.__class__}")

    try:
        thread1.join()
        thread2.join()
    except Exception as e:
        print(f"error is {e}        {e.__class__}")
    else:
        print("join threads complete")

    print(f"\n---HW1 result---")
    print(f"line_size : {line_size}")
    print(f"total line : {total_line} lines")
    print(f"number line over range : {line_over_range} lines")
    print(f"total over character : {total_over_char} characters")

    print(f"\n---HW2 result---")
    try:
        with open("./Homework/tahw_si_nohtyp.txt", "w",  encoding="utf-8") as f:
            for c in new_contents:
                for s in c:
                    f.write(s)
                    f.write(' ')
                f.write('\n')
    except Exception as e:
        print(e.__class__,e.args[1])
    else:
        print('File written successfully')
    print('Number of words not allowed')
    for d in n_word_dict:
        print(d, n_word_dict[d])

    print("\n---end---")

if __name__ == "__main__":
    main()