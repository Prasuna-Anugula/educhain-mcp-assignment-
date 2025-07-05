# Imports
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from educhain.core.config import LLMConfig            # Ensure this exists
from educhain.engines.content_engine import ContentEngine  # Import ContentEngine

# Define topic
print("Script started")
topic = "Cybersecurity"

# ---------------- MOCK LLM ----------------
class MockLLM(BaseLanguageModel):
    def _call(self, prompt: str, stop=None, **kwargs) -> str:
        import re
        
        match = re.search(r'"topic"\s*:\s*"([^"]+)"', prompt)
        topic = match.group(1).strip() if match else "Cybersecurity"

        return f'''
    {{
        "title": "Introduction to {topic}",
        "subject": "General Studies",
        "learning_objectives": [
            "Understand core concepts of {topic}",
            "Apply knowledge of {topic} to real-world examples",
            "Evaluate and reflect on key ideas within {topic}"
        ],
        "lesson_introduction": "This lesson introduces students to foundational ideas and real-world relevance of {topic}.",
        "main_topics": [
            {{
                "title": "{topic} Deep Dive",
                "subtopics": [
                    {{
                        "title": "Core Principles of {topic}",
                        "key_concepts": [
                            {{"type": "definition", "content": "Key terms and concepts in {topic}."}},
                            {{"type": "example", "content": "An everyday scenario involving {topic}."}}
                        ],
                        "discussion_questions": [
                            {{"question": "Why is {topic} important in today’s world?"}}
                        ],
                        "hands_on_activities": [
                            {{"title": "Explore {topic}", "description": "Group activity analyzing a real-world example of {topic}."}}
                        ],
                        "reflective_questions": [
                            {{"question": "How does {topic} affect you personally?"}}
                        ],
                        "assessment_ideas": [
                            {{"type": "project", "description": "Create a poster or presentation explaining {topic}."}}
                        ]
                    }}
                ]
            }}
        ],
        "learning_adaptations": "Provide scaffolding and support for learners new to {topic}.",
        "real_world_applications": "{topic} is used across industries and societal systems.",
        "ethical_considerations": "Explore potential ethical issues related to {topic}."
    }}
    '''



    @property
    def _llm_type(self) -> str:
        return "mock"

    def invoke(self, input, config=None, **kwargs):
        return AIMessage(content=self._call(str(input)))

    def predict(self, prompt: str, **kwargs):
        return self._call(prompt)

    def predict_messages(self, messages, **kwargs):
        return self._call(str(messages))

    def apredict(self, prompt: str, **kwargs):
        return self._call(prompt)

    def apredict_messages(self, messages, **kwargs):
        return self._call(str(messages))

    def generate_prompt(self, *args, **kwargs):
        return ChatResult(
            generations=[[ChatGeneration(message=AIMessage(content=self._call("mock prompt")))]]
        )

    async def agenerate_prompt(self, *args, **kwargs):
        return ChatResult(
            generations=[[ChatGeneration(message=AIMessage(content=self._call("async mock prompt")))]]
        )

    async def agenerate(self, messages, **kwargs):
        return AIMessage(content=self._call(str(messages)))

# ---------------- INIT CONTENT ENGINE ----------------

# Step 1: Create instance of MockLLM
mock_llm = MockLLM()

# Step 2: Wrap inside LLMConfig
mock_config = LLMConfig(custom_model=mock_llm)

# Step 3: Create ContentEngine using mock config
content_engine = ContentEngine(llm_config=mock_config)

# ---------------- USE IT ----------------

# Generate mock lesson plan
lesson_plan = content_engine.generate_lesson_plan(topic)

# Output the results
print("\nGenerated Lesson Plan:\n")
print(lesson_plan) 