class TitleTestAgent:
    def __init__(self):
        self.name = "Title Test Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Generating title variations...")

        titles = [
            "I Tried the Hardest Challenge in This Game",
            "This Gaming Challenge Was WAY Harder Than Expected",
            "I Thought I Could Beat This...",
            "The Craziest Moment Happened in This Game",
            "Can I Actually Beat This Challenge?",
            "This Went Completely Wrong",
            "I Was NOT Ready for This Gaming Moment",
            "The Most Unexpected Gameplay Moment",
            "One Mistake Changed Everything",
            "You Won't Expect What Happens Next"
        ]

        return {
            "status": "success",
            "agent": self.name,
            "titles": titles,
            "rules": [
                "Titles must accurately describe the video.",
                "Do not make false claims.",
                "Do not guarantee views or viral performance."
            ]
        }


if __name__ == "__main__":
    agent = TitleTestAgent()

    result = agent.run({
        "gameplay": "videos/gameplay.mp4"
    })

    print(result)