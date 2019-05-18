from collections import Counter

# https://stepik.org/lesson/13245/step/2?unit=3430


def encode_huffman(s):
    c = Counter(s)
    print(c)



    code = c
    return code


def main():
    s = input("Input str: ")
    code = encode_huffman(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{} : {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
