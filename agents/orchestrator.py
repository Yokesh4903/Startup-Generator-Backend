from agents.ceo import ceo_agent
from agents.marketing import marketing_agent
from agents.sales import sales_agent
from agents.hr import hr_agent
from agents.finance import finance_agent


def run_startup_simulator(business_idea, selected_agents=None):

    if selected_agents is None:
        selected_agents = [
            "CEO",
            "Marketing",
            "Sales",
            "HR",
            "Finance"
        ]

    result = {}

    if "CEO" in selected_agents:
        result["CEO"] = ceo_agent(business_idea)

    if "Marketing" in selected_agents:
        result["Marketing"] = marketing_agent(business_idea)

    if "Sales" in selected_agents:
        result["Sales"] = sales_agent(business_idea)

    if "HR" in selected_agents:
        result["HR"] = hr_agent(business_idea)

    if "Finance" in selected_agents:
        result["Finance"] = finance_agent(business_idea)

    return result