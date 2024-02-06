import autogen

config_list = [
    {
        
        'api_type': 'open_ai',
        'api_base': 'http://localhost:1234/v1',
        'api_key': 'NULL'
    }
]

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    code_execution_config={"work_dir":"web", "use_docker":"python:3"},
    system_message="You are a coder specializing in Python"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config= {"work_dir":"web", "use_docker":"python:3"},
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    #code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Write python code to output numbers 1 to 100, and then store the code in a file
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)
