class QualityAgent:
    def __init__(self):
        self.name = "Quality Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Checking project quality...")

        checks = {
            "gameplay_exists": bool(project.get("gameplay")),
            "video_exists": bool(project.get("video")),
            "metadata_exists": bool(project.get("metadata")),
            "fake_gameplay": False,
            "copyright_check": "pending"
        }

        critical_failed = (
            not checks["gameplay_exists"]
            or not checks["video_exists"]
            or not checks["metadata_exists"]
            or checks["fake_gameplay"]
        )

        return {
            "status": "FAIL" if critical_failed else "PASS",
            "agent": self.name,
            "checks": checks,
            "message": (
                "Critical quality check failed."
                if critical_failed
                else "Project passed the basic quality checks."
            )
        }


if __name__ == "__main__":
    agent = QualityAgent()

    result = agent.run({
        "gameplay": "videos/gameplay.mp4",
        "video": "output/final_video.mp4",
        "metadata": {
            "title": "Test Gaming Video"
        }
    })

    print(result)