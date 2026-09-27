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
        print("Running:", agent.name)
        result = agent.run(project)
        print(result)

    print("Workflow test completed.")


if __name__ == "__main__":
    main()