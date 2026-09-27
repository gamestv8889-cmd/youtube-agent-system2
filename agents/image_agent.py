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

        return {
            "status": "success",
            "agent": self.name,
            "images": [
                {
                    "type": "supporting_image",
                    "prompt": "Create a gaming-related supporting image based on the actual gameplay.",
                    "filename": "gameplay_support_01.png"
                },
                {
                    "type": "supporting_image",
                    "prompt": "Create a dramatic gaming visual relevant to the actual gameplay.",
                    "filename": "gameplay_support_