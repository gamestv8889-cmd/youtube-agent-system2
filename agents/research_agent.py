class ResearchAgent:
    def __init__(self):
        self.name = "Research Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Research started...")

        return {
            "status": "success",
            "agent": self.name,
            "research": {
                "audience": "US gaming audience",
                "topics": [],
                "trends": [],
                "keywords": [],
                "sources": []
            }
        }


if __name__ == "__main__":
    agent = ResearchAgent()

    result = agent.run({
        "type": "youtube_gameplay"
    })

    print(result)