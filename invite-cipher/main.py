table = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
    ["j", "k", "l", "m", "n", "o", "p", "q", "r"],
    ["s", "t", "u", "v", "w", "x", "y", "z", ""],
]

column = ["\U0001F44B", "\U0001F44A", "\U0001F44D", "\U0001F4AA", "\U0001F91F",
          "\U0001F466", "\U0001F467", "\U0001F44C", "\U0001F91E"]
row = ["\U0001F3FB", "\U0001F3FD", "\U0001F3FF"]

cipher_text = "your attendance at garage trip is the answer to the ultimate question of life, the universe, and everything"


def encode(text):
    mapping = {}
    for i in range(len(table)):
        for j in range(len(table[0])):
            if not table[i][j]:
                continue
            mapping[table[i][j]] = (j, i)

    cipher = []
    for c in text:
        m = mapping.get(c, None)
        if m is None:
            if c == " ":
                cipher.append("\n")
            else:
                cipher.append(c)
            continue
        cipher.append(column[m[0]])
        cipher.append(row[m[1]])

    # print(mapping)

    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(''.join(cipher))
    print(''.join(cipher))


if __name__ == '__main__':
    encode(cipher_text)
