# viya_rest_api

## link to postman collection:
https://www.getpostman.com/collections/f8c72d20ca9a5a00ec18

### Note:
### Import postman collection to your workspace
- import this postman collection by selecting "import", and paste the link above
- to execute sas job, first configure environment variables: base_url, job_url, and if applicable, macro varaible 
- you also need to set up your own authentication by editing the collection authentication


-----------------------------------------------------------------------------------------------------

## Prerequisites
1. Your SAS code saved as a viya job
2. Host url; job url; user crendentials including: username, password, clientsecret and clientID

## runSAS.py 
This makes the api calls to sasjobexecution, executes the sas code, and produces log.txt and output.html 

## config.py
config.py file is required to run the program ; please update config.py user credentials and host before running the code.


