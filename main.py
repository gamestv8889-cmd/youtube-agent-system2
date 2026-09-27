from agents.master_agent import MasterAgent
from agents.research_agent import ResearchAgent
from agents.script_agent import ScriptAgent
from agents.hook_agent import HookAgent
from agents.image_agent import ImageAgent
from agents.thumbnail_agent import ThumbnailAgent
from agents.editor_agent import EditorAgent
from agents.seo_agent import SEOAgent
from agents.quality_agent import QualityAgent


def main():
    print("YouTube Automation System started")
    print("=" * 40)

    project = {
        "gameplay": "videos/gameplay.mp4",
        "type": "youtube_gameplay",
        "audience": "US"
    }

    agents = [
        MasterAgent(),
        ResearchAgent(),
        ScriptAgent(),
        HookAgent(),
        ImageAgent(),
        ThumbnailAgent(),
        EditorAgent(),
        SEOAgent(),
        QualityAgent()
    ]

    for agent in agents:
        print(f"\nRunning: {agent.name}")

        try:
            result = agent.run(project)
            print(result)

        except Exception as error:
            print(f"ERROR in {agent.name}: {error}")

    print("\nWorkflow test completed.")


if __name__ == "__main__":
    main()