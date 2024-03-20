from random import choices, randint
from string import ascii_lowercase
from hashlib import sha256

def key_gen(lenght=10, word_len=3):
    words = ["".join(choices(ascii_lowercase, k=randint(3,lenght))) for _ in range(word_len)]
    phrase = " ".join(words)

    key = sha256(phrase.encode("utf-8")).hexdigest()

    return key

def edit_env(key):
    with open('.env', 'r+') as file:
        lines = file.readlines()

        for idx, line in enumerate(lines):
            if line.startswith("SECRET_KEY="):
                spliter = line.split("=")
                lines[idx] = spliter[0] + f'="{key}"\n'
                flag = True
        if flag:
            print(f"Successfully generate app key: {key}")
        else:
            print(f"Parameter 'SECRET_KEY' do not exist in '.env' file.")
        file.seek(0)
        file.writelines(lines)    

key = key_gen()
edit_env(key)
