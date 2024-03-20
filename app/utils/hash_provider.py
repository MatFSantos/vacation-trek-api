from hashlib import sha256

def generate(text: str) -> str:
    hash = sha256(text.encode("utf-8")).hexdigest()
    return hash

def verify(text: str, hash: str) -> bool:
    test = generate(text)
    return  test == hash