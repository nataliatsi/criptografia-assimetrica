import rsa

# gerar um par de chaves
publicKey, privateKey = rsa.newkeys(1024)

# salvar chave pública em um arquivo
with open('keys/publicKey.pem', 'wb') as p:
    p.write(publicKey.save_pkcs1('PEM'))



