class ShortsAgent:
    def __init__(self):
        self.name = "Shorts Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        gameplay = project.get("gameplay")

        if not gameplay:
            return {
                "status": "error",
                "message": "Gameplay file is missing"
            }

        print(f"[{self.name}] Preparing YouTube Shorts workflow...")

        return {
            "status": "success",
            "agent": self.name,
            "source": gameplay,
            "shorts_plan": {
                "format": "9:16",
                "duration_target": "under 60 seconds",
                "find_best_moment": True,
                "add_hook": True,
                "add_subtitles": True,
                "add_supporting_images": True,
                "output": "output/short.mp4"
            },
            "rules": [
                "Use real user-recorded gameplay.",
                "Do not invent gameplay moments.",
                "Keep the strongest moment near the beginning."
            ]
        }


if __name__