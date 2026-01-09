# pip install pycryptodome

import hashlib

def get_hash(text):
    # 해시 알고리즘 초기화
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    # 해시알고리즘 적용전 UTF-8인코등으로 전환
    uft8encoded = text.encode('utf-8')
    md5.update(uft8encoded)
    sha1.update(uft8encoded)
    sha256.update(uft8encoded)

    # 디지털지문 생성
    md5digest = md5.hexdigest()
    sha1digest = sha1.hexdigest()
    sha256digest = sha256.hexdigest()

    return md5digest, sha1digest, sha256digest

if __name__ == '__main__':
    text = 'hello, world!!'
    md5hashed, sha1hashed, sha256hashed = get_hash(text)
    print(md5hashed)
    print(sha1hashed)
    print(sha256hashed)

    text = 'Hello, World!!'
    md5hashed, sha1hashed, sha256hashed = get_hash(text)
    print(md5hashed)
    print(sha1hashed)
    print(sha256hashed)