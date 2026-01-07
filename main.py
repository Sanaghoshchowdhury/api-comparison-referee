from fastapi import FastAPI

app = FastAPI()

@app.get("/compare")
def compare_apis():
    return {
        "OpenAI API": {
            "Pros": [
                "Very powerful models",
                "Good documentation",
                "Easy to integrate"
            ],
            "Cons": [
                "Can be expensive",
                "Rate limits"
            ],
            "Best Use": "Chatbots, AI assistants, content generation"
        },
        "AWS Bedrock": {
            "Pros": [
                "Good security",
                "Enterprise ready",
                "Many foundation models"
            ],
            "Cons": [
                "More complex setup",
                "Learning curve"
            ],
            "Best Use": "Enterprise AI solutions"
        },
        "Anthropic Claude": {
            "Pros": [
                "Strong safety features",
                "Good long-context support"
            ],
            "Cons": [
                "Fewer integrations",
                "Limited regions"
            ],
            "Best Use": "Safe AI applications"
        }
    }
