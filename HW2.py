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

try:
    with open('./Homework/what_is_python.txt', 'r',encoding='utf-8') as f:
        contents = f.readlines()
        for line in contents:
            word = line.strip().split()
            new_word = []
            for w in word:
                new_word.append(reverse_word(w))
            new_contents.append(new_word)
except Exception as e:
    print(f"error is {e}        {e.__class__}")

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
    print('\nFile written successfully')

print('Number of words not allowed')
for d in n_word_dict:
    print(d, n_word_dict[d])