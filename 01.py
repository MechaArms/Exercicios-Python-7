#Exercicio 1
'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

def validaIP(ipAddress):
    blocos = ipAddress.split('.')
    for i in blocos:
        i = int(i)
        if i < 0 or i > 255:
            return False
    return True

with open("c:/Users/Suporte/Desktop/Python study/IP_entrada.txt", 'r') as arquivoEntrada: #abrindo o arquivo txt do exercicio é necessario criar o arquivo do enunciado
    linhas = arquivoEntrada.readlines()

ipsValidos = []
ipsInvalidos = []
for ip in linhas:
    if validaIP(ip) == True:
        ipsValidos.append(ip)
    else:
        ipsInvalidos.append(ip)

with open("c:/Users/Suporte/Desktop/Python study/IP_saida.txt", 'w') as arquivoSaida: #criando o arquivo  txt
    arquivoSaida.write('[IPs Validos]\n')
    for i in range(len(ipsValidos)):
        arquivoSaida.write(ipsValidos[i])
    arquivoSaida.write('\n[IPs Invalidos]\n')
    for i in range(len(ipsInvalidos)):
        arquivoSaida.write(ipsInvalidos[i])