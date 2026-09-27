class UploadAgent:
    def __init__(self):
        self.name = "Upload Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Preparing YouTube upload...")

        return {
            "status": "ready",
            "agent": self.name,
            "video": project.get("video", ""),
            "metadata": project.get("metadata", {}),
            "privacy": "private",
            "schedule": None,
            "message": "YouTube upload is not connected yet."
        }


if __name__ == "__main__":
    agent = UploadAgent()

    result = agent.run({
        "video": "output/final_video.mp4",
        "metadata": {}
    })

    print(result)