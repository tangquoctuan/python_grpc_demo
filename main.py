from __future__ import print_function

import grpc
from google.protobuf.json_format import MessageToDict

import settings_service_pb2 as settings_service
import settings_service_pb2_grpc as settings_service_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50000') as channel:
        stub = settings_service_grpc.SettingsServiceStub(channel)
        response_group_config = stub.GetConfigByGroup(settings_service.Config(group="REDIS"))
        dict_group_config = MessageToDict(response_group_config)["config"]
        for key, value in dict_group_config.iteritems():
            print(key)
            print(value["value"] if "value" in value else "")


if __name__ == '__main__':
    run()
