class ThumbnailAgent:
    def __init__(self):
        self.name = "Thumbnail Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Creating thumbnail concepts...")

        return {
            "status": "success",
            "agent": self.name,
            "concepts": [
                {
                    "style": "dramatic",
                    "text": "WHAT JUST HAPPENED?!",
                    "prompt": "Create a mobile-friendly gaming thumbnail based on the actual gameplay."
                },
                {
                    "style": "curiosity",
                    "text": "CAN I WIN?",
                    "prompt": "Create a high-contrast gaming thumbnail based only on the actual gameplay."
                },
                {
                    "style": "action",
                    "text": "INSANE MOMENT",
                    "prompt": "Create an exciting gaming thumbnail using the actual gameplay context."
                }
            ],
            "rules": [
                "Keep text short and readable on mobile.",
                "Do not show fake gameplay as real.",
                "Do not make misleading claims."
            ]
        }


if __name__ == "__main__":
    agent = ThumbnailAgent()

    result = agent.run({
        "gameplay": "user_recorded_gameplay.mp4"
    })

    print(result)