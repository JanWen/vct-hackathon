
import boto3
from botocore.exceptions import ClientError


client = boto3.client("bedrock-runtime", region_name="eu-central-1")
model_id = "amazon.titan-text-lite-v1"

def converse(text):
    # Start a conversation with the user message.
    user_message = text
    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]

    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId="amazon.titan-text-lite-v1",
            messages=conversation,
            inferenceConfig={"maxTokens":1024,"stopSequences":["User:"],"temperature":0,"topP":1},
            additionalModelRequestFields={}
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)
