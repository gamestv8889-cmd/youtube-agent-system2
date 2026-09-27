class HookAgent:
    def __init__(self):
        self.name = "Hook Agent"
        self.status = "ready"

    def run(self, project):
        if not project:
            return {
                "status": "error",
                "message": "Project data is missing"
            }

        print(f"[{self.name}] Creating hooks...")

        hooks = [
            "You won't believe what happened next...",
            "I thought this would be easy, but I was completely wrong.",
            "This was the craziest moment of the entire gameplay.",
            "Wait until you see what happens at the end.",
            "One mistake changed the whole game."
        ]

        return {
            "status": "success",
            "agent": self.name,
            "hooks": hooks,
            "recommended_hook": hooks[0]
        }


if __name__ == "__main__":
    agent = HookAgent()

    result = agent.run({
        "gameplay": "user_recorded_gameplay.mp4"
    })

    print(result)