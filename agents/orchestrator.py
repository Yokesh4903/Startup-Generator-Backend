from agents.ceo import ceo_agent
from agents.marketing import marketing_agent
from agents.sales import sales_agent
from agents.hr import hr_agent
from agents.finance import finance_agent


def run_startup_simulator(business_idea, selected_agents=None):

    print("Business Idea:", business_idea)
    print("Selected Agents:", selected_agents)

    if not selected_agents:
        selected_agents = [
            "CEO",
            # "Marketing",
            # "Sales",
            # "HR",
            # "Finance"
        ]

    print("After Default:", selected_agents)

    result = {}

    if "CEO" in selected_agents:
        print("Running CEO")
        result["CEO"] = ceo_agent(business_idea)

    if "Marketing" in selected_agents:
        print("Running Marketing")
        result["Marketing"] = marketing_agent(business_idea)

    if "Sales" in selected_agents:
        print("Running Sales")
        result["Sales"] = sales_agent(business_idea)

    if "HR" in selected_agents:
        print("Running HR")
        result["HR"] = hr_agent(business_idea)

    if "Finance" in selected_agents:
        print("Running Finance")
        result["Finance"] = finance_agent(business_idea)

    print(result)

    return result