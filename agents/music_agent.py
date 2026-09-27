class MusicAgent:
    def __init__(self):
        self.name = "Music Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Preparing music...")

        return {
            "status": "success",
            "agent": self.name,
            "music": {
                "source": "licensed_or_verified_library",
                "track": None,
                "volume": 0.15,
                "output": "assets/background_music.mp3"
            },
            "rules": [
                "Use only legally usable music.",
                "Verify the license before publishing.",
                "Do not claim music is copyright-free without verification.",
                "Keep music volume below the gameplay audio when appropriate."
            ]
        }


if __name__ == "__main__":
    agent = MusicAgent()

    result = agent.run({
        "video": "output/final_video.mp4"
    })

    print(result)