# generate client from proto file
python -m grpc_tools.protoc -I../grpcServer/Protos --python_out=. --grpc_python_out=. ../grpcServer/Protos/greet.proto

# open GUI
 ./grpcui -open-browser -plaintext localhost:5000