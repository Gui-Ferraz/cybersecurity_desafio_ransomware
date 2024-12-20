import os
import sys
import pyaes

# Pega o caminho do arquivo atraves do argumento passado 
if len(sys.argv) > 1:
    file_path = sys.argv[1]

# Usa o arquivo padrão
else:
    file_path = 'teste.txt.ransomwaretroll'

# Abrir e ler o conteúdo do arquivo
file = open(file_path, 'rb')
file_data = file.read()
file.close()

# Define a chave para a descriptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
data_decrypt = aes.decrypt(file_data)

# Deleta o arquivo criptografado
os.remove(file_path)

# Recria arquivo original
new_file_path = file_path.replace('.ransomwaretroll', '')
new_file = open(f'{new_file_path}', 'wb')
new_file.write(data_decrypt)
new_file.close()