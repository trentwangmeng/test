@ECHO OFF&PUSHD %~DP0 &TITLE ≤‚ ‘±®∏Ê
d: 
cd D:\codes\python_2020\App_UI_Automation
::del /F /A /Q /S Report
::rd /Q /S Report
::CLS
pytest
::CLS
call allure generate Report -o Report/html --clean
allure open Report/html
