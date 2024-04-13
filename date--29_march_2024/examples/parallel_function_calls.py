from openai import OpenAI
import json, os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})


def run_conversation():
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    print(f"Function Call 1st Response - {response}")
    '''
    ChatCompletion(
        id='chatcmpl-9CHROUjsWCnqXwWKHzdjrcixdZntM',
        choices=[
            Choice(
                finish_reason='tool_calls',
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content=None,
                    role='assistant',
                    function_call=None,
                    tool_calls=[
                        ChatCompletionMessageToolCall(
                            id='call_5A0TeB7RYMacgCNbId6NR0Gb',
                            function=Function(
                                arguments='{"location": "San Francisco", "unit": "celsius"}',
                                name='get_current_weather'
                            ),
                            type='function'
                        ),
                        ChatCompletionMessageToolCall(
                            id='call_Sp7Xi5M1trPulcALfQyme3MX',
                            function=Function(
                                arguments='{"location": "Tokyo", "unit": "celsius"}',
                                name='get_current_weather'
                            ),
                            type='function'
                        ),
                        ChatCompletionMessageToolCall(
                            id='call_1v5lYRl6Vm3dH2RGO3GZzc5T',
                            function=Function(
                                arguments='{"location": "Paris", "unit": "celsius"}',
                                name='get_current_weather'
                            ),
                        type='function'
                    )
                    ]
                )
            )
            ],
            created=1712714006,
            model='gpt-3.5-turbo-0125',
            object='chat.completion',
            system_fingerprint='fp_b28b39ffa8',
            usage=CompletionUsage(
                completion_tokens=77,
                prompt_tokens=88,
                total_tokens=165
            )
        )
    '''

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response


print(run_conversation())
'''
ChatCompletion(
    id='chatcmpl-9CHNZWHBnPN8DBAFn9Zwehq0duhu2',
    choices=[
        Choice(
            finish_reason='stop',
            index=0,
            logprobs=None,
            message=
                ChatCompletionMessage(
                    content="The current weather in San Francisco is 72°F, in Tokyo it's 10°C, and in Paris it's 22°C.",
                    role='assistant',
                    function_call=None,
                    tool_calls=None
                )
            )
        ],
    created=1712713769,
    model='gpt-3.5-turbo-0125',
    object='chat.completion',
    system_fingerprint='fp_b28b39ffa8',
    usage=CompletionUsage(
        completion_tokens=28,
        prompt_tokens=147,
        total_tokens=175
        )
    )

'''