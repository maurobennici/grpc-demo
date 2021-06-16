import logging
import datetime

import grpc

import greet_pb2
import greet_pb2_grpc

def run():
  
  a = datetime.datetime.now()
  
  x = range(1000)
  for n in x:
    channel = grpc.insecure_channel('localhost:5000')
    stub = greet_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(greet_pb2.HelloRequest(name='Mauro'))
    print("Greeter client received: " + response.message)

    channel = grpc.insecure_channel('localhost:5000')
    stub = greet_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(greet_pb2.HelloRequest(name='Savi'))
    print("Greeter client received: " + response.message)

  b = datetime.datetime.now()
  print(b-a)

if __name__ == '__main__':
    logging.basicConfig()
    run()