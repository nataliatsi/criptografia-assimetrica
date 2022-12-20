import rsa
from zipfile import ZipFile
from hashlib import sha256
from script1 import privateKey
from script2 import *


# abrir arquivos compactados
with ZipFile('compactados.zip', 'r') as zip:
    zip.extractall('descompactados')

# ler arquivo de texto e gerar hash
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
hash = getHashFromFile('descompactados/texto/mensagem.txt')
hashcode2 = hash
# descriptografar com a chave privada
decmsg = rsa.decrypt(encmsg, privateKey).decode()

# gerar arquivo de texto com hash descriptografado
with open('descompactados/texto/hashdescompactado.txt', 'w') as d:
    d.write(decmsg)

# comparar hash do programa 'A' com do programa atual ('B')
if (hashcode2 == decmsg):
    print('Arquivo Autêntico!')
else: 
    print('Arquivo Não Autêntico!')

