class Compress:
    def compress(self, string: str):
        token_table = {}
        token_stream = []
        count = 1
        for word in string.split(" "):
            # Agregar token a la tabla
            if word not in token_table:
                token_table[word] = count
                count += 1

            # Agregar token al comprimido
            token_stream.append(token_table[word])
        
        return token_stream, token_table

    def uncompress(self, token_stream, token_table) -> str:
        inverted_dict = {value: key for key, value in token_table.items()}
        string = ""
        for token in token_stream:
            string += inverted_dict[token] + " "
        return string.strip()


if __name__ == "__main__":
    c = Compress()
    for file in ["ci.txt", "ct.txt", "cv.txt", "oop.txt", "tdd.txt"]:
        with open(file) as f:
            text = f.read()
            compressed, values = c.compress(text)
            string = c.uncompress(compressed, values)
