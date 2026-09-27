import os


class SecurityAgent:
    def __init__(self):
        self.name = "Security Agent"
        self.status = "ready"

    def run(self, project=None):
        print(f"[{self.name}] Checking security...")

        required_secrets = [
            "OPENAI_API_KEY",
            "YOUTUBE_CLIENT_ID",
            "YOUTUBE_CLIENT_SECRET"
        ]

        missing = [
            secret
            for secret in required_secrets
            if not os.getenv(secret)
        ]

        if missing:
            return {
                "status": "warning",
                "agent": self.name,
                "missing_secrets": missing,
                "message": "Required secrets are not configured yet."
            }

        return {
            "status": "PASS",
            "agent": self.name,
            "message": "Required environment secrets are available."
        }


if __name__ == "__main__":
    agent = SecurityAgent()

    result = agent.run()

    print(result)