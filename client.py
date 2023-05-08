import socket
import time

# cria um objeto socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define o endereço do servidor e a porta que ele está escutando
server_address = ('localhost', 7642)

# define os tamanhos de pacotes a serem testados
packet_sizes = [64, 128, 256, 512, 1024]

for size in packet_sizes:
    # envia uma mensagem de teste para o servidor com o tamanho correspondente
    message = "M" * size
    start = time.time()
    sock.sendto(message.encode(), server_address)

    # aguarda receber a resposta do servidor
    data, _ = sock.recvfrom(4096)
    end = time.time()

    # exibe o tempo de resposta do servidor
    print("Tamanho do pacote: {} bytes | Tempo de resposta do servidor: {:.6f}s".format(size, end - start))

# fecha o socket
sock.close()