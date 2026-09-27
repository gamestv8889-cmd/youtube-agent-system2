class PublishCheckAgent:
    def __init__(self):
        self.name = "Publish Check Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Running final publish checks...")

        checks = {
            "gameplay": bool(project.get("gameplay")),
            "final_video": bool(project