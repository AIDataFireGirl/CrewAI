from crewai import Task

class TravelTasks:
    def __init__(self, agents):
        self.agents = agents

    def analyze_preferences(self, user_preferences):
        """Task for analyzing user travel preferences"""
        return Task(
            description=f"""Analyze the following user preferences and create a detailed 
            understanding of their travel needs:
            {user_preferences}
            
            Consider:
            1. Travel style and preferences
            2. Must-visit locations
            3. Special requirements or constraints
            4. Preferred activities
            """,
            agent=self.agents.travel_agent
        )

    def create_budget(self, preferences_analysis):
        """Task for creating a detailed budget plan"""
        return Task(
            description=f"""Based on the following preferences analysis, create a detailed 
            budget plan:
            {preferences_analysis}
            
            Include:
            1. Transportation costs
            2. Accommodation costs
            3. Activity costs
            4. Food and dining budget
            5. Emergency fund
            """,
            agent=self.agents.budget_agent
        )

    def create_itinerary(self, preferences_analysis, budget_plan):
        """Task for creating a detailed itinerary"""
        return Task(
            description=f"""Create a detailed day-by-day itinerary based on:
            Preferences: {preferences_analysis}
            Budget: {budget_plan}
            
            Include:
            1. Daily schedule
            2. Transportation details
            3. Activity timings
            4. Restaurant recommendations
            5. Free time suggestions
            """,
            agent=self.agents.itinerary_agent
        )

    def create_final_plan(self, preferences, budget, itinerary):
        """Task for creating the final comprehensive plan"""
        return Task(
            description=f"""Create a comprehensive final trip plan combining:
            Preferences: {preferences}
            Budget: {budget}
            Itinerary: {itinerary}
            
            The final plan should include:
            1. Executive summary
            2. Detailed itinerary
            3. Budget breakdown
            4. Important contacts
            5. Emergency information
            6. Packing suggestions
            """,
            agent=self.agents.final_planner
        ) 