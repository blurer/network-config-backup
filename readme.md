# Network Configuration Backup

This pythons script will input a csv file expecting the headers "hostname" and "ip address" and then login to each device. While the script is running it will create a new file called results.csv that'll include the status of the save and the date. 

## NOTES ##
- You should be using getpass and never hard coding the username/password. 
- Adjust the tftp server as yours 

## Automation ##
The best way to automate this is via cron, here is an example that'll attach the results.csv and email it:
``0 0 * * 0 /usr/bin/python /path/to/myscript.py && uuencode /path/to/results.csv results.csv | mail -s "Cron Job Results" -a "Content-Type: text/csv" myemail@example.com``
