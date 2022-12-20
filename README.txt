# IFPB - Guarabira

--- Avaliação 2: Criptografia Assimétrica

Componente Curricular: Segurança da Informação
Professor: George Candeia de Sousa Medeiros
Alunas: Natália Dos Santos Gomes (202023810004)
        Nielen Jhose Mendes e Silva (202113810037)
Turma: TSI - 4º período

>> Linguagem de programação: Python
>> Bibliotecas usadas:  hashlib, rsa, zipfile e shutil

>> Funcionamento:

# script1:
+ gerar um par de chaves (pública e privada)
+ exportar a chave pública para um arquivo do tipo PEM

# script2:
+ gerar hash a partir de um arquivo de texto
+ encripitar hash gerado
+ exportar hash encriptado para um arquivo txt
+ compactar pasta com os seguintes arquivos:
        ++ texto original 
        ++ hash criptografado

# script3:
+ descompactar arquivos
+ gerar um novo hash para o mesmo arquivo de texto (mensagem)
+ descriptografar hash
+ exportar hash descriptografado para um arquivo txt
+ comparar hash gerado (hashcode2) com hash descriptografado (decmsg)

>> Ordem de execução:

1. script1
2. script2
3. script3

>> Observações:

- não foi possível testar a alteração no arquivo com o hash gerado no script3, para verificar o erro de não autênticidade.