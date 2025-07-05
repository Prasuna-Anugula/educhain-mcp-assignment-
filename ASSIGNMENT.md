#  Educhain Internship Assignment Submission

This repository contains a minimal working prototype of an MCP server integrated with the Educhain library. It was developed as part of an internship assignment.

---

## 🔍 Objective

To simulate lesson plan generation using the Educhain content engine and expose the functionality through a locally running MCP-compatible server.



## MockLLM Usage

To avoid dependency on external APIs (like OpenAI or Google Gemini), a `MockLLM` was implemented using `langchain_core.BaseLanguageModel`.

- This allows fully **offline** and **deterministic** testing.
- It returns static lesson plan data structured as expected by Educhain.
- Ensures compatibility with `ContentEngine.generate_lesson_plan(...)`.

---

## Key Files

| File                          | Purpose                                         |
|-------------------------------|-------------------------------------------------|
| `test_python.py`              | Main script to test Educhain with MockLLM      |
| `mcp_server/server.py`        | Flask server exposing lesson plan endpoint      |
| `Sample_Responses.txt`        | Sample API responses (e.g., lesson plan JSON)   |
| `claude_desktop_config.json`  | Claude Desktop integration config               |
| `README.md`                   | Original Educhain documentation (retained)      |

---

## 🔧 How to Run the Test

```bash
# Install dependencies
pip install -r requirements.txt

# Run the test script
python test_python.py
```

---

## Notes

- The core Educhain repo and docs are **unaltered** and kept for reference.
- Only testing tools and local integration logic were added.
- No API keys are required to test this version.

---

## Submission
## Tool Testing Note

Due to Claude Desktop not recognizing my tool via MCP config in time for the deadline, I implemented and tested the lesson plan endpoint using:

- A mock LLM (via `educhain_wrapper.py`)
- A Flask server exposing `/generate_lesson_plan`
- Postman and terminal tests to verify the response
- Sample response is attached in `Sample_Responses.txt`

All components are working correctly except Claude's tool discovery, which appears to be a local config issue.


