# Import socket module
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import socket
import json
import GameEngineGroupA
import ast

class Server():
    def __init__(self, address, port=3000):
        # Create a socket object
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to the server on local computer
        self.s.bind((address, port))
        print("Set up for ip", address, " using port ", port)

    def accept(self):
        """
        Here the server accepts a new request
        """
        self.s.listen(5)
        self.s, self.addr = self.s.accept()

    def recv(self):
        """
        Here the game engine waits for a message from the platform
        :return: message, a json object
        """
        print("Move recieved")
        message = self.s.recv(1024)
        return message

    def send(self, message):
        """
        Here the game engine sends a response
        param: message, a json message
        """
        self.s.send(message)
        print("Move sent")

    def close(self):
        self.s.close()

    def is_json(self, myjson):
        """
        checking to see if a file is a json
        """
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True


if __name__ == "__main__":
    print("hello")

    ip = input('please enter servers IP address: ')
    serv = Server(ip)
    msg = None
    serv.accept()
    while (True):

        byte_msg = serv.recv()
        msg = json.loads(byte_msg.decode('utf-8'))
        msg["Board"] = {x:y for x,y in enumerate(msg["Board"],0)}
        #msg = byte_msg.decode('utf8').replace("'", '"')

        print(msg)
        # msg = {int(k):v for k,v in msg["Board"].items()}

        if msg == "end":
            break
        with open('board.json', 'w', encoding='utf-8') as f:
            json.dump(msg, f)
        GameEngineGroupA.runUUGame('board.json')
        with open ('board.json', 'r', encoding='utf-8') as f:
            ai_msg = json.load(f)
        keys = list(msg['Board'].keys())
        print("Keys", keys)
        # json_ai_msg = json.dumps(ai_msg)
        ai_msg = json.dumps(ai_msg)
        print(ai_msg)
        byte_ai_msg = bytes(ai_msg, encoding='utf-8')
        serv.send(byte_ai_msg)

    serv.close()
