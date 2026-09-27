class ImageAgent:
    def __init__(self):
        self.name = "Image Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Preparing image prompts...")

        images = [
            {
                "type": "supporting_image",
                "prompt": (
                    "Create a gaming-related supporting image "
                    "based on the actual gameplay."
                ),
                "filename": "gameplay_support_01.png"
            },
            {
                "type": "supporting_image",
                "prompt": (
                    "Create a dramatic gaming visual "
                    "relevant to the actual gameplay."
                ),
                "filename": "gameplay_support_02.png"
            }
        ]

        return {
            "status": "success",
            "agent": self.name,
            "images": images,
            "rule": (
                "AI images are supporting assets and must not "
                "be presented as real gameplay."
            )
        }


if __name__ == "__main__":
    agent = ImageAgent()

    result = agent.run({
        "gameplay": "videos/gameplay.mp4"
    })

    print(result)