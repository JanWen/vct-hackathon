
import boto3
from botocore.exceptions import ClientError


client = boto3.client("bedrock-runtime", region_name="eu-central-1")
model_id = "anthropic.claude-v2"

system_prompt = [{
    "text": "You are Yapperino, a helpful assistant focues on anwsering questions about professional Valorant esports.",
}]

def converse(text):
    # Start a conversation with the user message.
    user_message = text
    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]
    print(conversation)
    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens":1024,"stopSequences":["User:"],"temperature":0,"topP":1},
            additionalModelRequestFields={},
            system=system_prompt,
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)


def converse_new(conversation_log: list[(str, str)]):    
    conversation = [{
        "role": i[0],
        "content": [{"text": i[1]}],
    } for i in conversation_log]

    print(conversation)
    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens":1024,"stopSequences":["User:"],"temperature":0,"topP":1},
            additionalModelRequestFields={},
            system=system_prompt,
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)