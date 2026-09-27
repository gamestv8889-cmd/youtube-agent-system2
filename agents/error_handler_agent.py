class ErrorHandlerAgent:
    def __init__(self):
        self.name = "Error Handler Agent"
        self.status = "ready"

    def run(self, error_data):
        if not error_data:
            return {
                "status": "error",
                "message": "Error data is missing"
            }

        error_type = error_data.get("type", "unknown")
        message = error_data.get("message", "Unknown error")
        retries = error_data.get("retries", 0)

        print(f"[{self.name}] Handling error: {error_type}")

        temporary_errors = [
            "network",
            "timeout",
            "rate_limit",
            "temporary"
        ]

        if error_type in temporary_errors and retries < 3:
            action = "retry"
        else:
            action = "stop_and_report"

        return {
            "status": "handled",
            "agent": self.name,
            "error_type": error_type,
            "message": message,
            "retries": retries,
            "action": action
        }


if __name__ == "__main__":
    agent = ErrorHandlerAgent()

    result = agent.run({
        "type": "network",
        "message": "Connection failed",
        "retries": 0
    })

    print(result)