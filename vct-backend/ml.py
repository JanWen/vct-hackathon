
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


def converse_agent(session_id, text):
    # invoke aws berock agent

    response = agent.invoke_agent(
        agentAliasId="JALFJNCRF1",
        agentId="DHEBFNZFA9",
        sessionId=session_id,
        inputText=text,
    )
    print(response)

    completion = response["completion"]
    response_text = []
    for i in completion:
        if "chunk" in i:
            print("CHUNK: ", i["chunk"]["bytes"])
            response_text.append(str(i["chunk"]["bytes"], "utf-8"))
        elif "trace" in i:
            trace = i["trace"]["trace"]
            if "failureTrace" in trace:
                print("FAILURE TRACE: ", trace["failureTrace"]["failureReason"])
            else:
                print(trace)
        else:
            print(i)


    return "\n".join(response_text)