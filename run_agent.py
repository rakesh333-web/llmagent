from llm_agents import Agent, ChatLLM, PythonREPLTool, SerpAPITool

if __name__ == '__main__':
    prompt = input("Enter a question / task for the agent: ")
    agent = Agent(
        tools=[PythonREPLTool(), SerpAPITool()]
    )
    result = agent.run(prompt)

    print(f"Final answer is {result}")

