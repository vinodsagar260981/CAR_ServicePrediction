from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class MaintenanceState(TypedDict):
    vehicle_id: str
    diagnosis: dict
    documents: list
    explanation: str


class PredictiveMaintenanceAgent:

    def __init__(self, rule_service, retriever, llm_service):

        self.rule_service = rule_service
        self.retriever = retriever
        self.llm_service = llm_service

        graph = StateGraph(MaintenanceState)

        graph.add_node("diagnose", self.diagnose)
        graph.add_node("retrieve", self.retrieve)
        graph.add_node("explain", self.explain)

        graph.add_edge(START, "diagnose")
        graph.add_edge("diagnose", "retrieve")
        graph.add_edge("retrieve", "explain")
        graph.add_edge("explain", END)

        self.graph = graph.compile()

    def diagnose(self, state: MaintenanceState):

        diagnosis = self.rule_service.analyze_vehicle(
            state["vehicle_id"]
        )

        return {
            "diagnosis": diagnosis
        }

    def retrieve(self, state: MaintenanceState):

        diagnosis = state["diagnosis"]

        alerts = "\n".join(
                str(alert)
                for alert in diagnosis["alerts"]
            )

        query = f"""
            Vehicle maintenance diagnosis:

            Status: {diagnosis["status"]}

            Conditions:
            {alerts}

            Provide relevant automotive engineering
            maintenance and diagnostic information.
            """

        documents = self.retriever.retrieve(query)

        return {
            "documents": documents
        }

    def explain(self, state: MaintenanceState):

        explanation = self.llm_service.explain_diagnosis(
            state["diagnosis"],
            state["documents"]
        )

        return {
            "explanation": explanation
        }

    def run(self, vehicle_id: str):

        result = self.graph.invoke({
            "vehicle_id": vehicle_id
        }) # type: ignore

        return {
            **result["diagnosis"],
            "explanation": result["explanation"]
        }