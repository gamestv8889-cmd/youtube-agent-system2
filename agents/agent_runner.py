class AgentRunner:
    def __init__(self):
        self.agents = {}

    def register(self, name, agent):
        self.agents[name] = agent

    def run(self, name, data=None):
        if name not in self.agents:
            raise ValueError(f"Agent not found: {name}")

        agent = self.agents[name]
        return agent(data)


def example_agent(data):
    return {
        "status": "success",
        "data": data
    }


if __name__ == "__main__":
    runner = AgentRunner()

    runner.register("example", example_agent)

    result = runner.run("example", {
        "message": "Agent system is working"
    })

    print(result)