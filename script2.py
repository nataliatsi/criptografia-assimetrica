import rsa, shutil
from hashlib import md5, sha256
from script1 import publicKey

# função para gerar hash do arquivo de texto
def getHashFromFile(file):
    hash = sha256()
    b = bytearray(128*1024)
    mv =  memoryview(b)
    with open(file, "rb", buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            hash.update(mv[:n])
    return hash.hexdigest()

# chamada da função
hash = getHashFromFile('texto/mensagem.txt')
hashcode1 = hash

# criptografar hash
encmsg = rsa.encrypt(hash.encode(), publicKey)

# gerar arquivo de texto com hash criptografado
with open('texto/hashcode.txt', 'wb') as h:
    h.write(encmsg)

# criar pacote RAR com o arquivo de texto e hash criptografado
shutil.make_archive('compactados', 'zip', './', 'texto')


