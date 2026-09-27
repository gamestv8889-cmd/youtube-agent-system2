from datetime import datetime


class ReportAgent:
    def __init__(self):
        self.name = "Report Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Creating project report...")

        return {
            "status": "success",
            "agent": self.name,
            "report": {
                "project_id": project.get("project_id", "unknown"),
                "created_at": datetime.now().isoformat(),
                "agent_status": project.get("agent_status", {}),
                "quality": project.get("quality", {}),
                "upload": project.get("upload", {}),
                "schedule": project.get("schedule", {}),
                "errors": project.get("errors", [])
            }
        }


if __name__ == "__main__":
    agent = ReportAgent()

    result = agent.run({
        "project_id": "test-project",
        "agent_status": {},
        "quality": {},
        "upload": {},
        "schedule": {},
        "errors": []
    })

    print(result)