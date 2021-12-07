# exchenge-python-bot
A very simple script for alerting in telegram from special exchange dir

## how you can use it
If you need telegram alert about anything and you can't create telegram bot on your infrastructure, but you have e-mail alerts.
You can:
1. Do filter in you mail. Save special mails in special exchange dir.
2. Use this script. It connect to you mailbox from anywhere, read special dir and forward alert in telegram

## requirements
exchangelib 4.6.1
requests 2.26.0

## quick start
1. do pip install -r requirements.txt
2. implement you properties in config/config.ini
3. **important**: implement your exchange dir in main.py#20 (Yep, It is hardcode, because I'm tired) 

## troubleshooting
If you have any troubles, you can create issue. I try to help.
