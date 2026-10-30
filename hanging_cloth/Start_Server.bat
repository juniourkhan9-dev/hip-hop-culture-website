@echo off
title Hanging Cloth Showcase Server
echo Starting Hanging Cloth Showcase on http://localhost:3001 ...
start http://localhost:3001
python -m http.server 3001
pause
