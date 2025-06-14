from crewai import Crew
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv
import os
import sys

def load_environment():
    """Load environment variables and validate required settings"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Check for required environment variables
    required_vars = ['OPENAI_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"- {var}")
        print("\nPlease create a .env file with these variables. See .env.example for a template.")
        sys.exit(1)
    
    # Get optional environment variables with defaults
    config = {
        'model': os.getenv('OPENAI_MODEL', 'gpt-4'),
        'temperature': float(os.getenv('TEMPERATURE', '0.7')),
        'max_tokens': int(os.getenv('MAX_TOKENS', '2000')),
        'timeout': int(os.getenv('TIMEOUT', '60'))
    }
    
    return config

def plan_vacation(user_preferences):
    """
    Main function to plan a vacation using CrewAI agents
    
    Args:
        user_preferences (str): User's travel preferences and requirements
    """
    # Load and validate environment variables
    config = load_environment()
    
    # Initialize agents
    agents = TravelAgents()
    
    # Initialize tasks
    tasks = TravelTasks(agents)
    
    # Create the crew
    crew = Crew(
        agents=[
            agents.travel_agent,
            agents.budget_agent,
            agents.itinerary_agent,
            agents.final_planner
        ],
        tasks=[
            tasks.analyze_preferences(user_preferences),
            tasks.create_budget("Based on preferences analysis"),
            tasks.create_itinerary("Based on preferences", "Based on budget"),
            tasks.create_final_plan("Final preferences", "Final budget", "Final itinerary")
        ],
        verbose=True
    )
    
    # Execute the crew's tasks
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    # Example user preferences
    sample_preferences = """
    I want to plan a 7-day trip to Japan in the spring.
    Budget: $3000
    Interests: Food, culture, and nature
    Must-visit: Tokyo, Kyoto, and Mount Fuji
    Travel style: Mix of luxury and local experiences
    Special requirements: Vegetarian food options
    """
    
    try:
        # Get the vacation plan
        vacation_plan = plan_vacation(sample_preferences)
        
        # Print the result
        print("\n=== Your Vacation Plan ===")
        print(vacation_plan)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1) 