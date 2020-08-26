#import requests and json modules
import requests as request
import json
import time
import config

base_url =config.base_url


def token():
    username =config.username
    password = config.password
    oAuthCliendId =config.oAuthCliendId
    oAuthClientSecret =config.oAuthClientSecret
    
    # build full API URL
    # seperate .py program
    url = base_url + '/SASLogon/oauth/token'

    # pass headers to API
    headers = { 
        'content-type': 'application/x-www-form-urlencoded' 
        }
    payload = 'grant_type=password&username=' + username + '&password=' + password
    r = request.post(url, payload, headers=headers, auth=(oAuthCliendId, oAuthClientSecret))
    responseObj = json.loads(r.text)
    oAuthAccessToken = responseObj['access_token']
    return oAuthAccessToken

def runCode(jobName, macro):

#   url= base_url + '/SASJobExecution?_program=%2FPublic%2F'+jobName+'&param='+macro
    url= base_url + '/SASJobExecution/?_program=/Users/sawang/My%20Folder/testFolder/'+jobName+'&param='+macro
    oAuthAccessToken = token();
    headers = {
      'Authorization': 'bearer ' + oAuthAccessToken,
      'Content-Type': 'application/vnd.sas.job.execution.job.request',
      'Accept': 'application/vnd.sas.job.execution.job'
    }

    r = request.post(url, data=None, headers = headers)
    return r.text

def log_html(response):
    log_str =response.split('<iframe ', 1)[0]+ response.split('</iframe>', 1)[1]

    filename = "Log_"+time.strftime("%Y%m%d-%H%M%S")+".html"
    with open(filename, "w") as log_html:
        log_html.write(log_str)
        
        
def output_html(response):
    output_url =response.split('src="', 1)[1].split("\"></iframe>", 1)[0]
    url = base_url + output_url
    
    oAuthAccessToken = token();

    headers = {
      'Authorization': 'bearer ' + oAuthAccessToken
    }
    # get full output html
    r = request.get(url, data=None, headers = headers)
    html_str = r.text
    # convert str to output.html
    filename = "Output_"+time.strftime("%Y%m%d-%H%M%S")+".html"

    with open(filename, "w") as output_html:
        output_html.write(html_str)