#import requests and json modules
import requests as request
import json
import time
import config

#import config variables
base_url =config.base_url
job_url =config.job_url
username =config.username
password = config.password
oAuthCliendId =config.oAuthCliendId
oAuthClientSecret =config.oAuthClientSecret
# macro ='MSRP'

#generate token
url = base_url + '/SASLogon/oauth/token'

# pass headers to API
headers = { 
    'content-type': 'application/x-www-form-urlencoded' 
    }
payload = 'grant_type=password&username=' + username + '&password=' + password
r = request.post(url, payload, headers=headers, auth=(oAuthCliendId, oAuthClientSecret))
responseObj = json.loads(r.text)
oAuthAccessToken = responseObj['access_token']

# submit job
url= job_url +'&_action=json&_resultfile=*&_omittextlog=false'
# url= job_url +'&param='+macro + '&_action=json&_resultfile=*&_omittextlog=false'
headers = {
  'Authorization': 'bearer ' + oAuthAccessToken,
  'Content-Type': 'application/vnd.sas.job.execution.job.request',
  'Accept': 'application/vnd.sas.job.execution.job'
}

r = request.post(url, headers = headers).json()
print(r)

#construct url to retrieve log and output table
log_uri= base_url+ r[1]['href']
output_uri = base_url +  r[2]['href']

#generate log file
log_str = request.get(log_uri, headers = headers).text

filename = "Log_"+time.strftime("%Y%m%d-%H%M%S")+".txt"
with open(filename, "w") as log:
    log.write(log_str)


#generate output table(s) file
output_str = request.get(output_uri, headers = headers).text
filename ="Output_"+time.strftime("%Y%m%d-%H%M%S")+".html"
with open(filename, "w") as output_html:
    output_html.write(output_str)
