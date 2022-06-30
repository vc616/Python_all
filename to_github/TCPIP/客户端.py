import socket
if __name__ == '__main__':
    # 1 创建客户端套接字对象tcp_client_1
    # 参数介绍：AF_INET 代表IPV4类型, SOCK_STREAM代表tcp传输协议类型 ,注：AF_INET6代表IPV6
    # 2 通过客户端套接字的connect方法与服务器套接字建立连接  
    # 参数介绍：前面的ip地址代表服务器的ip地址，后面的61234代表服务端的端口号 。
    while 1:
        s = input("输入要发送的内容：")
        s = "客户端A："+ s
        tcp_client_1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_client_1.connect(("192.168.6.7",61234))

        # 将编号好的数据存到变量send_data中，注：encode(encoding='utf-8)是将数据转换成utf-8的格式发送给服务器
        send_data = s.encode(encoding='utf-8')
        
        # 3 通过客户端套接字的send方法将数据发送给服务器
        tcp_client_1.send(send_data)

        # 4 通过客户端套接字的recv方法来接受服务器返回的数据存到变量recv_data中，1024是可接收的最大字节数。
        recv_data = tcp_client_1.recv(1024)
        
        # 将接收到的服务器数据recv_data通过decode方法解码为utf-8
        print(recv_data.decode(encoding = 'utf-8'))

        # 5 最后关闭客户端套接字连接
        tcp_client_1.close()

