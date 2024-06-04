@echo off
:: Define paths
set BASE_DOWNLOAD_PATH=PATH
set PYTHON_SCRIPT_PATH=PATH

:: Run the yt-dlp batch script
call .\download_playlists.bat

:: Run the Python script to update metadata
python "%PYTHON_SCRIPT_PATH%"
