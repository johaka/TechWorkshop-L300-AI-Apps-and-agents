# Azure imports
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation.red_team import RedTeam, RiskCategory, AttackStrategy
from pyrit.prompt_target import OpenAIChatTarget
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

# Azure AI Project Information
azure_ai_project = os.getenv("AZURE_AI_AGENT_ENDPOINT")

# Instantiate your AI Red Teaming Agent
# For 1 2 3 use cases, uncomment the respective section below
# red_team_agent = RedTeam(
#     azure_ai_project=azure_ai_project,
#     credential=DefaultAzureCredential(),
#     risk_categories=[
#         RiskCategory.Violence,
#         RiskCategory.HateUnfairness,
#         RiskCategory.Sexual,
#         RiskCategory.SelfHarm
#     ],
#     num_objectives=5,
# )
 
# For 4
red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project,
    credential=DefaultAzureCredential(),
    custom_attack_seed_prompts="data/custom_attack_prompts.json",
)

 



#1 Test chat target function
# def test_chat_target(query: str) -> str:
#     return "I am a simple AI assistant that follows ethical guidelines. I'm sorry, Dave. I'm afraid I can't do that."
# Configuration for Azure OpenAI model

#2 Test with Azure OpenAI model
#  azure_openai_config = {
#     "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
#     "api_key": os.environ.get("AZURE_OPENAI_KEY"),
#     "azure_deployment": os.environ.get("AZURE_OPENAI_API_VERSION"),
# }

#3 GPT-4.1 Chat Target
chat_target = OpenAIChatTarget(
    model_name=os.environ.get("gpt_deployment"),
    endpoint=os.environ.get("gpt_endpoint"),
    api_key=os.environ.get("gpt_api_key"),
    api_version=os.environ.get("gpt_api_version"),
) 


async def main():
    #1 red_team_result = await red_team_agent.scan(target=test_chat_target)
    #2 red_team_result = await red_team_agent.scan(target=azure_openai_config)
    #3 and 4 red_team_result = await red_team_agent.scan(target=chat_target)
    #5 Below
    # red_team_result = await red_team_agent.scan(
    #     target=chat_target,
    #     scan_name="Red Team Scan - Easy Strategies",
    #     attack_strategies=[
    #         AttackStrategy.EASY
    #     ])

    #6 Below
    red_team_result = await red_team_agent.scan(
        target=chat_target,
        scan_name="Red Team Scan - Easy-Moderate Strategies",
        attack_strategies=[
            AttackStrategy.Flip,
            AttackStrategy.ROT13,
            AttackStrategy.Base64,
            AttackStrategy.AnsiAttack,
            AttackStrategy.Tense
        ])



asyncio.run(main())
