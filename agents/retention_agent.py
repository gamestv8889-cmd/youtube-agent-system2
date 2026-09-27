class RetentionAgent:
    def __init__(self):
        self.name = "Retention Agent"
        self.status = "ready"

    def run(self, analytics):
        if analytics is None:
            return {
                "status": "error",
                "message": "Analytics data is missing"
            }

        print(f"[{self.name}] Analyzing audience retention...")

        retention = analytics.get("retention", [])

        if not retention:
            return {
                "status": "success",
                "agent": self.name,
                "status_detail": "waiting_for_retention_data",
                "dropoffs": [],
                "insights": [
                    "No retention data is available yet."
                ]
            }

        dropoffs = []

        for point in retention:
            if point.get("change", 0) < -10:
                dropoffs.append(point)

        return {
            "status": "success",
            "agent": self.name,
            "dropoffs": dropoffs,
            "insights": [
                "Investigate major retention drops.",
                "Compare drops with the video timeline.",
                "Do not assume a cause without supporting data."
            ]
        }


if __name__ == "__main__":
    agent = RetentionAgent()

    result = agent.run({
        "retention": [
            {"time": "0:10", "change": -5},
            {"time": "0:30", "change": -15}
        ]
    })

    print(result)