# Python NebriOS Authentication

The simple and easy-to-use package for making authenticated NebriOS api requests from a python application.

This app is intended for use with a NebriOS instance. Visit https://nebrios.com to sign up for free!

<h2>Installation</h2>

This app can be installed via PyPi:
```
pip install git+https://github.com/briem-bixly/python-nebrios-authentication#egg=python-nebrios-authentication
```

<strong>NOTE</strong>: This app requires https://github.com/brie-bixly/python-nebrios.

<strong>NOTE</strong>: Before using any classes and associated functions in this package, you must include nebrios-authentication in your NebriOS Instance and set up any authentication methods you would like to utilize. See https://github.com/briem-bixly/nebrios-authentication/blob/master/README.md for more information.

<h2>Public Classes</h2>
<strong>NebriOSToken</strong>
This is the most basic authentication method supported. This class must be instantiated before use.
```
token_client = NebriOSToken('instance_name', 'token')
```
- instance name is your NebriOS instance name. i.e. https://<strong>instance_name</strong>.nebrios.com
- your token must be generated on your NebriOS instance using https://github.com/briem-bixly/nebrios-authentication

<strong>NebriOSBasic</strong>
```
basic_client = NebriOSBasic('instance_name', 'username', 'password')
```
- before using this method, a username and password combo should be saved to your NebriOS instance using https://github.com/briem-bixly/nebrios-authentication

<strong>NebriOSOAuth</strong>
```
oauth_client = NebriOSOAuth('instance_name', access_token='access_token', consumer_key='consumer_key', consumer_secret='consumer_secret')
```
- consumer key and consumer secret should be obtained from your NebriOS instance using https://github.com/briem-bixly/nebrios-authentication
- if you have already created an access token, consumer key and consumer secret are not required
- if you have not created an access token, only consumer key and consumer secret are required. this app will make the appropriate call for an access token and will save the generated token to your NebriOSAuth instance automatically.

<h2>Public Function</h2>
All classes have the same function with the same parameters.

<strong>api_request</strong>
- api_module: the name of the api module stored on your NebriOS instance
- view_name: the name of the target function contained in the given api module
- method: the desired HTTP request method
- headers (optional): any custom headers you would like added to your request
- payload (optional): an object containing params and values
- files (optional): any files that you would like to upload via a POST request

<h2>Examples</h2>
```
from nebrios_auth import NebriOSToken
token_client = NebriOSToken('instance_name', 'token')
token_client.api_request('api_module', 'view_name', method='POST', payload=payload)
//outputs response
```
```
from nebrios_auth import NebriOSBasic
basic_client = NebriOSBasic('instance_name', 'username', 'password')
basic_client.api_request('api_module', 'view_name', method='POST', payload=payload)
//outputs response
```
```
from nebrios_auth import NebriOSOAuth
oauth_client = NebriOSOAuth('instance_name', consumer_key='consumer_key', consumer_secret='consumer_secret')
oauth_client.api_request('api_module', 'view_name', method='POST', payload=payload)
//outputs response
```
```
from nebrios_auth import NebriOSOAuth
oauth_client = NebriOSOAuth('instance_name', access_token='access_token')
oauth_client.api_request('api_module', 'view_name', method='POST', payload=payload)
//outputs response
```
