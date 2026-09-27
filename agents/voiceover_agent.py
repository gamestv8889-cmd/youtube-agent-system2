class VoiceoverAgent:
    def __init__(self):
        self.name = "Voiceover Agent"
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

        print(f"[{self.name}] Preparing voiceover...")

        return {
            "status": "success",
            "agent": self.name,
            "voiceover": {
                "language": "en-US",
                "script": script,
                "voice": "default",
                "output": "assets/voiceover.mp3"
            },
            "rules": [
                "Use authorized AI/TTS voice only.",
                "Do not imitate a real person without permission.",
                "Keep narration synchronized with gameplay."
            ]
        }


if __name__ == "__main__":
    agent = VoiceoverAgent()

    result = agent.run({
        "script": "This is a test gaming voiceover."
    })

    print(result)