class AnalyticsAgent:
    def __init__(self):
        self.name = "Analytics Agent"
        self.status = "ready"

    def run(self, data):
        if not data:
            return {
                "status": "error",
                "message": "Analytics data is missing"
            }

        print(f"[{self.name}] Analyzing YouTube data...")

        metrics = {
            "views": data.get("views", 0),
            "impressions": data.get("impressions", 0),
            "ctr": data.get("ctr", 0),
            "watch_time": data.get("watch_time", 0),
            "average_view_duration": data.get(
                "average_view_duration", 0
            ),
            "likes": data.get("likes", 0),
            "comments": data.get("comments", 0)
        }

        return {
            "status": "success",
            "agent": self.name,
            "metrics": metrics,
            "insights": [
                "Compare current performance with previous videos.",
                "Identify retention and engagement changes.",
                "Do not invent missing metrics."
            ]
        }


if __name__ == "__main__":
    agent = AnalyticsAgent()

    result = agent.run({
        "views": 0,
        "impressions": 0,
        "ctr": 0,
        "watch_time": 0,
        "average_view_duration": 0,
        "likes": 0,
        "comments": 0
    })

    print(result)