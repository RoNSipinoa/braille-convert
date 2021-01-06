def braille_decompose():
    braille_list = []
    output_list = []
    output_string = ''
    for i in input('점자를 입력해 주세요.   '):
        braille_list.append(i)
    for i in braille_list:
        a = ord(i) - 10240
        braille_string = ''
        for j in range(8, 0, -1):
            if a - 2 ** (j - 1) >= 0:
                braille_string = str(j) + braille_string
                a -= 2 ** (j - 1)
            else:
                pass
        if a == 0:
            braille_string = '0'
        output_list.append(braille_string)
    for i in output_list:
        output_string += i + ' '
    print(output_string)

def braille_compose(message):
    a = input('점자 번호를 입력해 주세요.   ').split()
    output_string = ''
    for i in a:
        n = 0
        i = list(set(i))
        for j in i:
            if int(j) not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                raise ValueError
            if int(j) == 0:
                n = 0
            else:
                n += 2 ** (int(j) - 1)
        output_string += chr(10240 + n)
    print(output_string)
