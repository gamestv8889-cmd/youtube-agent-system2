class SubtitleAgent:
    def __init__(self):
        self.name = "Subtitle Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        script = project.get("script", "")

        if not script:
            return {
                "status": "error",
                "message": "Script is missing"
            }

        print(f"[{self.name}] Preparing subtitles...")

        return {
            "status": "success",
            "agent": self.name,
            "subtitle": {
                "language": "en-US",
                "format": "srt",
                "text": script,
                "output": "assets/subtitles.srt"
            },
            "rules": [
                "Keep subtitles synchronized with the video.",
                "Use short, readable lines.",
                "Do not invent dialogue."
            ]
        }


if __name__ == "__main__":
    agent = SubtitleAgent()

    result = agent.run({
        "script": "This is a test subtitle."
    })

    print(result)