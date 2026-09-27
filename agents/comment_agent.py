class CommentAgent:
    def __init__(self):
        self.name = "Comment Agent"
        self.status = "ready"

    def run(self, comments):
        if comments is None:
            return {
                "status": "error",
                "message": "Comments data is missing"
            }

        print(f"[{self.name}] Analyzing comments...")

        replies = []

        for comment in comments:
            replies.append({
                "comment": comment,
                "suggested_reply": "Thanks for watching! 🔥",
                "approved": False
            })

        return {
            "status": "success",
            "agent": self.name,
            "replies": replies,
            "rules": [
                "Never post replies automatically without authorization.",
                "Do not reveal private information.",
                "Keep replies respectful and relevant."
            ]
        }


if __name__ == "__main__":
    agent = CommentAgent()

    result = agent.run([
        "Great video!",
        "How did you do that?"
    ])

    print(result)