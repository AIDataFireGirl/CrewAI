from crewai import Agent
from langchain.tools import tool

class TravelAgents:
    def __init__(self):
        # Initialize the travel agent
        self.travel_agent = Agent(
            role='Travel Preferences Specialist',
            goal='Analyze and understand user travel preferences to create the best possible trip plan',
            backstory="""You are an experienced travel agent with years of experience in 
            understanding client preferences and creating personalized travel experiences.""",
            verbose=True,
            allow_delegation=True
        )

        # Initialize the budget agent
        self.budget_agent = Agent(
            role='Budget Planning Specialist',
            goal='Create a detailed budget plan that aligns with user preferences and constraints',
            backstory="""You are a financial expert specializing in travel budgeting. 
            You know how to optimize costs while maintaining quality experiences.""",
            verbose=True,
            allow_delegation=True
        )

        # Initialize the itinerary agent
        self.itinerary_agent = Agent(
            role='Itinerary Planning Specialist',
            goal='Create detailed day-by-day itineraries that maximize the travel experience',
            backstory="""You are a travel itinerary expert who knows how to create 
            perfect schedules that balance activities, rest, and local experiences.""",
            verbose=True,
            allow_delegation=True
        )

        # Initialize the final planner agent
        self.final_planner = Agent(
            role='Final Trip Planner',
            goal='Combine all information into a comprehensive and cohesive trip plan',
            backstory="""You are a master trip planner who excels at combining different 
            aspects of travel planning into a perfect final plan.""",
            verbose=True,
            allow_delegation=True
        ) 