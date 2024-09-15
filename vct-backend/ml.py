
import boto3
from botocore.exceptions import ClientError


client = boto3.client("bedrock-runtime", region_name="eu-central-1")
model_id = "amazon.titan-text-lite-v1"

agent = boto3.client('bedrock-agent-runtime')

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


def converse_agent(text):
    # invoke aws berock agent

    response = agent.invoke_agent(
        agentAliasId="9KFXEZVX3C",
        agentId="LWB33VIRAO",
        sessionId="asdasd",
        inputText="tell me about the vct and all the regions in it",
    )
    print(response)

    completion = response["completion"]
    for i in completion:
        print(i)

converse_agent("ayosjj")