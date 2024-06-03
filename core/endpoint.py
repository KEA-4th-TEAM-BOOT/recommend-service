import boto3
import json

def query_endpoint_embedding_with_json_payload(encoded_json, endpoint_name, content_type="application/json"):
    client = boto3.client("runtime.sagemaker")
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=content_type, Body=encoded_json
    )
    return response

def transform_output(output: bytes) -> str:
    response_json = json.loads(output.read().decode("utf-8"))
    # return response_json
    return response_json[0][0]