def numeric_encoding(str):
    str_list = []
    # 分组
    for i in range(0, len(str), 3):
        print(str[i:i+3])
        str_list.append(str[i:i+3])
        code = ''
        for i in str_list:
            rqbin_len = 10
            if len(i) == 1:
                rqbin_len = 4

            elif len(i) == 2:
                rqbin_len = 7

            code_temp = bin(int(i))[2:]
            code += ('0'*(rqbin_len - len(code_temp)) + code_temp)
            return code


if __name__ == '__main__':
    # out = numeric_encoding("12345678")
    # print(out)
    print(bin(16)[2:])
