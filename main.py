#!usr/bin/env python3
import paramiko
import csv
import datetime

# create a new SSH client
client = paramiko.SSHClient()

# open the CSV file that will store the results
results_file = open("results.csv", "w")
writer = csv.DictWriter(results_file, ["hostname", "ip_address", "date", "status"])
writer.writeheader()

# use the SSH client to connect to each Cisco device in the list
with open("cisco_devices.csv") as f:
    # use the csv module to parse the CSV file
    reader = csv.DictReader(f)

    for row in reader:
        # get the IP address and hostname of the device
        ip_address = row["ip_address"]
        hostname = row["hostname"]

        print("Connecting to device {} at IP address {}".format(hostname, ip_address))

        # connect to the device using the default username and password
        client.connect(ip_address, username="cisco", password="cisco")

        # create a file name that includes the hostname and current date
        now = datetime.datetime.now()
        filename = "{}-{}.config".format(hostname, now.strftime("%Y%m%d"))

        # use the 'copy running-config tftp' command to save the configuration to the TFTP server
        # replace "10.1.1.10" with the IP address of your TFTP server
        try:
            client.exec_command("copy running-config tftp://10.1.1.10/{}".format(filename))
            status = "pass"
        except:
            status = "fail"

        # write the hostname, IP address, and status to the results file
        writer.writerow({"hostname": hostname, "ip_address": ip_address, "status": status, "date": now.strftime("%Y%m%d")})

        # disconnect from the device
        client.close()

# close the results file
results_file.close()
