class SEOAgent:
    def __init__(self):
        self.name = "SEO Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Preparing YouTube metadata...")

        return {
            "status": "success",
            "agent": self.name,
            "metadata": {
                "title": "INSANE Gaming Moment You Won't Expect!",
                "description": (
                    "Watch this gameplay and see how the match unfolds. "
                    "Subscribe for more gaming videos."
                ),
                "keywords": [
                    "gaming",
                    "gameplay",
                    "gaming shorts",
                    "US gaming",
                    "funny gaming"
                ],
                "hashtags": [
                    "#gaming",
                    "#gameplay",
                    "#shorts"
                ],
                "language": "en-US"
            },
            "rules": [
                "Use accurate metadata.",
                "Do not use unrelated keywords.",
                "Do not make misleading claims."
            ]
        }


if __name__ == "__main__":
    agent = SEOAgent()

    result = agent.run({
        "gameplay": "videos/gameplay.mp4"
    })

    print(result)