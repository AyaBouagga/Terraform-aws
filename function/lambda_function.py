import json
import os
import logging
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests.auth import HTTPBasicAuth

# Initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Retrieve OpenSearch endpoint from the environment variable
OPENSEARCH_ENDPOINT = os.environ['OPENSEARCH_ENDPOINT']
OPENSEARCH_USER = os.environ['OPENSEARCH_USER']  # For basic auth if required
OPENSEARCH_PASSWORD = os.environ['OPENSEARCH_PASSWORD']  # For basic auth if required

# Initialize OpenSearch client
client = OpenSearch(
    hosts = [OPENSEARCH_ENDPOINT],
    http_auth = HTTPBasicAuth(OPENSEARCH_USER, OPENSEARCH_PASSWORD),  # Authentication if needed
    use_ssl = True,
    verify_certs = True,
    connection_class=RequestsHttpConnection,
)

# Function to index data into OpenSearch
def index_data_to_opensearch(data):
    index_name = 'logs-index'  # Index name in OpenSearch
    try:
        response = client.index(
            index=index_name,
            body=data,
            refresh=True  # Refresh to make the document searchable immediately
        )
        logger.info(f"Document indexed with ID: {response['_id']}")
        return response
    except Exception as e:
        logger.error(f"Error indexing data to OpenSearch: {str(e)}")
        raise

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event))

    # Simulate receiving data from the event (can be customized based on your use case)
    document = {
        "user": "lambda_user",
        "message": "This is a professional test message from Lambda!",
        "timestamp": "2024-11-24T00:00:00",
        "event_source": event.get("source", "unknown"),
    }

    # Validate document data
    if not document.get("user") or not document.get("message"):
        logger.error("Missing required fields in the document.")
        return {
            'statusCode': 400,
            'body': json.dumps('Bad Request: Missing required fields.')
        }

    # Send the data to OpenSearch
    try:
        response = index_data_to_opensearch(document)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data successfully indexed in OpenSearch!',
                'document_id': response['_id']
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }