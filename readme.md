# Network Configuration Backup

This pythons script will input a csv file expecting the headers "hostname" and "ip address" and then login to each device. While the script is running it will create a new file called results.csv that'll include the status of the save and the date. 

## NOTE ##
You should be using getpass in place of hard coding the username/password. 