from datetime import datetime


class TrendMonitorAgent:
    def __init__(self):
        self.name = "Trend Monitor Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Monitoring trends...")

        return {
            "status": "success",
            "agent": self.name,
            "checked_at": datetime.now().isoformat(),
            "region": "US",
            "platform": "YouTube",
            "trends": [],
            "sources": [],
            "rules": [
                "Use current and verifiable trend data.",
                "Record the source and date for each trend.",
                "Never invent trend information."
            ]
        }


if __name__ == "__main__":
    agent = TrendMonitorAgent()

    result = agent.run({
        "niche": "gaming"
    })

    print(result)