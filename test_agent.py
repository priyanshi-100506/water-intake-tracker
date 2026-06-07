from src.agent import WaterIntakeAgent

print("Initializing AI Agent...\n")

agent = WaterIntakeAgent()

water_intake = 1200

print(f"Analyzing {water_intake} mL water intake...\n")

response = agent.analyze_intake(water_intake)

print("AI Feedback:\n")
print(response)