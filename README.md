# API Comparison Tool – The Referee

This project is an API Comparison Tool created for Week 6: “The Referee” challenge. The goal of this project is to help users compare multiple APIs and understand their trade-offs instead of giving a single “best” answer.

The tool compares three popular AI APIs: OpenAI API, AWS Bedrock, and Anthropic Claude API. It clearly explains the pros, cons, cost considerations, and typical use cases of each API so that users can make their own informed decision.

Many beginners and developers struggle to choose the right API because different APIs are good at different things. Most existing solutions simply recommend one option without explaining why. This project solves that problem by acting as a neutral referee that presents all options fairly.

The project is built using a simple and beginner-friendly tech stack. The backend is written in Python using FastAPI, the frontend uses basic HTML and JavaScript, and Kiro is used to generate and structure the API comparisons. GitHub is used for version control and project sharing.

The folder structure of the project is simple and organized. It includes a backend folder containing the FastAPI code, a frontend folder containing the HTML file for the user interface, a .kiro folder that stores the Kiro prompt used for generating comparisons, and this README file.

Kiro played an important role in accelerating development. It was used to quickly generate structured comparisons between APIs, identify pros and cons, and explain trade-offs clearly. Using Kiro reduced the time spent on manual research and helped ensure consistent and well-organized outputs. Screenshots of Kiro prompts and responses are included in the AWS Builder Center technical blog as proof of implementation.

To run the project, first install the required Python packages using pip install fastapi uvicorn. Then start the backend server using uvicorn backend.main:app --reload. After the server starts, open the frontend/index.html file in a web browser and click the “Compare APIs” button to view the comparison results. No API keys are required to run this project.

This project was submitted as part of the AI for Bharat program. A detailed technical blog explaining the problem, solution, architecture, and how Kiro accelerated development has been published on AWS Builder Center. The GitHub repository link and the blog link were submitted through the participant dashboard before the weekly deadline.

Author: Sana Ghosh Chowdhury  
Program: AI for Bharat  
Purpose: Educational and learning use only
