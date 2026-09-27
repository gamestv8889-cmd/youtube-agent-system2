import os
import shutil


class BackupAgent:
    def __init__(self):
        self.name = "Backup Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        source = project.get("gameplay")

        if not source:
            return {
                "status": "error",
                "message": "Original gameplay path is missing"
            }

        backup_folder = "backups"
        os.makedirs(backup_folder, exist_ok=True)

        if not os.path.exists(source):
            return {
                "status": "error",
                "message": f"Gameplay file not found: {source}"
            }

        filename = os.path.basename(source)
        destination = os.path.join(backup_folder, filename)

        shutil.copy2(source, destination)

        print(f"[{self.name}] Backup created: {destination}")

        return {
            "status": "success",
            "agent": self.name,
            "backup": destination,
            "message": "Original gameplay backed up successfully."
        }


if __name__ == "__main__":
    agent = BackupAgent()

    result = agent.run({
        "gameplay": "videos/gameplay.mp4"
    })

    print(result)