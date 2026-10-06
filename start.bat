@echo off
title ORBITRA'26 WebGL Local Server
cd /d "%~dp0"

where node >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Starting server with Node.js...
    start http://localhost:3000
    node serve.js
    goto end
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Starting server with Python...
    start http://localhost:3000
    python server.py
    goto end
)

echo Neither Node.js nor Python was found in PATH.
pause

:end
