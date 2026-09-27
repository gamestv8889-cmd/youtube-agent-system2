import os


class AssetManagerAgent:
    def __init__(self):
        self.name = "Asset Manager Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Managing project assets...")

        folders = [
            "videos",
            "assets",
            "assets/images",
            "assets/audio",
            "assets/subtitles",
            "output",
            "backups"
        ]

        created = []

        for folder in folders:
            os.makedirs(folder, exist_ok=True)
            created.append(folder)

        return {
            "status": "success",
            "agent": self.name,
            "folders": created,
            "rules": [
                "Never delete the original gameplay.",
                "Keep project assets organized.",
                "Keep final videos in the output folder."
            ]
        }


if __name__ == "__main__":
    agent = AssetManagerAgent()

    result = agent.run({
        "project": "youtube_gameplay"
    })

    print(result)