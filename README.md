# python_grpc_demo
Demo code call grpc from python server
Step to build
1. Copy 2 files name: {name}_pb2.py and {name}_pb2_grpc.py to python project
2. See more main.py to understand how python server call grpc.
  - using lib from google.protobuf.json_format import MessageToDict to parse message recevice from grpc to dict.
