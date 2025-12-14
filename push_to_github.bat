@echo off
set GIT_CMD="C:\Program Files\Git\cmd\git.exe"

echo Initializing Git repository...
%GIT_CMD% init
%GIT_CMD% config user.email "bot@example.com"
%GIT_CMD% config user.name "AI Assistant"
%GIT_CMD% add .
%GIT_CMD% commit -m "Add Cloud Deployment Configs (Render/Heroku)"
%GIT_CMD% branch -M main
%GIT_CMD% remote remove origin
%GIT_CMD% remote add origin https://github.com/AK-2110/Initial-release-of-LinkedIn-Insights-Microservice.git
echo Pushing to GitHub...
%GIT_CMD% push -u origin main
echo Done!
pause
