REM This is an example of how to set AWS credentials using setx in a Windows batch file.
REM Replace the placeholder values with your actual AWS credentials.
REM run in terminal as: ./set-aws-creds.bat


@echo off
REM Set persistent AWS credentials on Windows

setx AWS_ACCESS_KEY_ID "XXXXXXXXXXXXXXX"
setx AWS_SECRET_ACCESS_KEY "XXXXXXXXXXXXXXXXXXXXXXX"
setx AWS_SESSION_TOKEN "XXXXXXXXXXXXXXXXXXXX"
setx AWS_DEFAULT_REGION "us-west-2"

echo.
echo ✅ AWS credentials set using setx.
echo ⚠️  You may need to restart your terminal for changes to take effect.
pause
REM End of script