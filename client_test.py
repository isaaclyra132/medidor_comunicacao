import socket
import time
import csv

# cria um objeto socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define o endereço do servidor e a porta que ele está escutando
server_address = ("localhost", 7642)
# server_address = ("192.168.1.105", 7642)

# define os tamanhos de pacotes a serem testados
packet_sizes = [64, 128, 256, 512, 1024]

# define o número de tentativas por tamanho de pacote
num_trials = 30

# cria um dicionário para armazenar os tempos de resposta para cada tamanho de pacote
response_times = {size: [] for size in packet_sizes}

for size in packet_sizes:
    for i in range(num_trials):
        # envia uma mensagem de teste para o servidor com o tamanho correspondente
        message = "M" * size
        start = time.time()
        sock.sendto(message.encode(), server_address)

        # aguarda receber a resposta do servidor
        data, _ = sock.recvfrom(4096)
        end = time.time()

        # armazena o tempo de resposta no dicionário
        response_times[size].append((end - start) * 1000)

print(response_times)
# cria um arquivo CSV para armazenar os tempos de resposta
with open("PC1_response_times.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # escreve o cabeçalho do arquivo CSV
    writer.writerow(["Nº Iteração"] + packet_sizes)

    # escreve os tempos de resposta para cada tamanho de pacote em colunas separadas
    for i in range(num_trials):
        row = [i + 1] + [
            "{:.6f}".format(response_times[size][i]) for size in packet_sizes
        ]
        writer.writerow(row)

# fecha o socket
sock.close()
