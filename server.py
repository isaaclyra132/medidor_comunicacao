import socket

# cria um objeto socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define o endereço do servidor e a porta que ele irá escutar
server_address = ("localhost", 7642)
# server_address = ("192.168.1.105", 7642)
sock.bind(server_address)

while True:
    # aguarda receber um pacote de dados do cliente
    data, address = sock.recvfrom(4096)

    # processa a mensagem recebida
    message = data.decode()
    response = "Olá, " + message
    print(response)

    # envia a resposta de volta para o cliente
    sock.sendto(response.encode(), address)
