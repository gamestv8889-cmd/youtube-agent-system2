from datetime import datetime


class ScheduleAgent:
    def __init__(self):
        self.name = "Schedule Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Preparing publishing schedule...")

        scheduled_time = project.get("scheduled_time")

        if not scheduled_time:
            scheduled_time = datetime.now().isoformat()

        return {
            "status": "success",
            "agent": self.name,
            "scheduled_time": scheduled_time,
            "timezone": "Asia/Tashkent",
            "approved": False,
            "message": "Schedule prepared. Publishing requires final approval."
        }


if __name__ == "__main__":
    agent = ScheduleAgent()

    result = agent.run({
        "scheduled_time": None
    })

    print(result)