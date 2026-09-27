class IdeaAgent:
    def __init__(self):
        self.name = "Idea Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Generating video ideas...")

        return {
            "status": "success",
            "agent": self.name,
            "ideas": [
                {
                    "title": "Can I Beat This Impossible Challenge?",
                    "hook": "I thought this would be easy...",
                    "gameplay_needed": True,
                    "supporting_images": True
                },
                {
                    "title": "The Craziest Thing Happened in This Game",
                    "hook": "You won't believe what happened next.",
                    "gameplay_needed": True,
                    "supporting_images": True
                },
                {
                    "title": "I Tried the Hardest Challenge",
                    "hook": "One mistake could ruin everything.",
                    "gameplay_needed": True,
                    "supporting_images": False
                }
            ],
            "rules": [
                "Ideas must fit the actual gameplay.",
                "Do not invent gameplay events.",
                "Keep concepts original."
            ]
        }


if __name__ == "__main__":
    agent = IdeaAgent()

    result = agent.run({
        "game": "gaming",
        "audience": "US"
    })

    print(result)