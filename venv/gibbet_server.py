import random
import  socketserver

class MyTPCHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()

        print ('Клиент собрался поиграть', self.data)
        x = random.randint(1,100)
        if self.data == 'START':
            print ('Клиент собрался поиграть', self.data)
            try.count()
            self.request.sendall ('GUESS;1;100')
            
if __name__ == '__main__' :
    HOST\
        = 'localhost'
    PORT = 9999
    server = socketserver.TCPServer((HOST,PORT), MyTPCHandler)
    print ('Сервер запущен')
    server.serve_forever()
