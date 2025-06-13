🚀 Lab 2 – Jenkins Integration with GitHub (CI/CD Pipeline)
✅ Approach Used
Implemented polling-based integration between GitHub and Jenkins.

Configured Jenkins to poll GitHub every 5 minutes using:

groovy
Copy
Edit
pollSCM('H/5 * * * *')
🛠️ Project Description
Created a simple Python app (app.py) with a greet() function.

Wrote a unit test (test_app.py) using Python’s built-in unittest.

requirements.txt includes:

txt
Copy
Edit
pytest
🔗 Jenkins & GitHub Setup
Connected Jenkins to GitHub using a Personal Access Token (PAT).

Configured to monitor the main branch of the repo.

GitHub repo URL used in Jenkins:

bash
Copy
Edit
https://github.com/Durlabh8972/python-ci-cd-Jenkins-lab2.git

📋 Jenkins Pipeline Stages
Checkout: Clones the GitHub repository.

Install Dependencies: Installs pip packages and checks Python version.

Build: Simulates a build step using an echo.

Test: Runs unit tests using unittest.

Notify: Outputs a build success message (email notification optional).

🧪 Testing & Results
Made small changes in the repo (e.g., README edit).

Jenkins detected the change and triggered the build automatically.

All pipeline stages executed successfully.

⚙️ Challenges & Fixes
Jenkins didn’t recognize python → Fixed by ensuring Python is in the system PATH.

Handled missing requirements.txt gracefully with fallback messages.

Resolved missing test file error by verifying the file structure.

📌 Summary
This lab demonstrated end-to-end CI/CD automation using Jenkins and GitHub. The polling method ensures regular checks for changes, while the pipeline ensures code quality with every update.
