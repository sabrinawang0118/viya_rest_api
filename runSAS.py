#import requests and json modules
import main

#Authenticate and obtain access token: 
oAuthAccessToken= main.token()

# Select job to run; change to your jobname in viya 
jobName = "yourJobName"

# pass in macro
# Example: MSRP, Invoice, EngineSize, Cylinders
macro = "yourMacrovariable"

# run sas9 code
response = main.runCode(jobName, macro)

#generate output.html for easy viewing
main.output_html(response)

#save SAS log into log.html for easy viewing
main.log_html(response)