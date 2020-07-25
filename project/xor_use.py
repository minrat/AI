'''
    XOR 按位异或，相同为 0，不同为 1
    加密：a ^ b ^ key = a ^ (b ^ key) = (a ^ b) ^ key
    解密：(a ^ key) ^ key = a ^ (key ^ key) = a ^ 0 = a
        对两者进行异或操作，计算解密出来的 int 对象所占比特数。
        decrypted.bit_length 函数得到的是二进制数的位数，除以 8 可以得到所占比特大小。
        为了防止，1 ~ 7 位的二进制数整除 8 得到 0，所以要加上 7，然后再进行整除 8 的操作。
        使用 int.to_bytes 函数将解密之后的 int 的对象转换成 bytes 对象。最后通过 decode 方法，将[字节串]转换成[字符串]。
'''


class XOR:
    def __init__(self):
        try:
            with open('encrypt_key_file') as encrypt_key_file:
                self.xor = encrypt_key_file.read()
        except FileNotFoundError as e:
            print("No Exist Key , Re-Generate Key")
            self.xor = self.generate_random_key(1024)

    def generate_random_key(self, key_length):
        from secrets import token_bytes
        key = token_bytes(nbytes=key_length)
        random_key = int.from_bytes(key, 'big')
        with open("encrypt_key_file", "w") as x:
            x.write(str(random_key))
        return random_key

    def encrypt_common(self, content):
        raw_bytes = content.encode('utf-8')
        raw_int = int.from_bytes(raw_bytes, 'big')
        encrypt_result = raw_int ^ int(self.xor)
        return encrypt_result

    def decrypt_common(self, content):
        decrypted = int(content) ^ int(self.xor)
        length = (decrypted.bit_length() + 7) // 8
        decrypted_bytes = int.to_bytes(decrypted, length, 'big')
        decrypt_result = decrypted_bytes.decode()
        return decrypt_result


if __name__ == '__main__':
    demo = XOR()
    msg = "I Like Python"
    out = demo.encrypt_common(msg)
    print("Target: "+str(out))
    back = demo.decrypt_common(out)
    print("Source: "+back)
