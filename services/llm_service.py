from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class LLMService:

    def __init__(self):
        self.llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0
        )

    def explain_diagnosis(self, diagnosis, documents):

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        alerts = "\n".join(
            str(alert)
            for alert in diagnosis["alerts"]
        )

        prompt = f"""
        You are an automotive maintenance engineer.

        Vehicle:
        {diagnosis["vehicle_id"]}

        Diagnosis:
        {diagnosis["status"]}

        Detected conditions:
        {alerts}

        Engineering knowledge:
        {context}

        Explain the detected conditions using only
        the engineering knowledge provided.

        Do not invent faults.
        Do not claim that a component has failed.
        Recommend relevant inspection areas.
        Keep the explanation concise and technical.
        """

        response = self.llm.invoke(prompt)

        return response.content