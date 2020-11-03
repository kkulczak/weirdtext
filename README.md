# Weired-Text
Weirdtext translation service.

The is deployed on Heroku and can be accessed under this address: https://kkulczak-weird-text.herokuapp.com/

## Deployment
Deployment is performed automatically, after every push to `master` branch and success status from github tests actions.

# API Documentation Example
This API uses `POST` request to communicate and HTTP [response codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) to indenticate status and errors. All responses come in standard JSON. All requests must include a `content-type` of `application/json` and the body must be valid JSON.

## Response Codes 
### Response Codes
```
200: Success
400: Bad request
50X: Server Error
```
## Encode Message
**You send:**  Message to be encoded.

**You get:** Encoded message.

**Request:**
```json
POST /v1/encode HTTP/1.1
Accept: application/json
Content-Type: application/json
Content-Length: xy

{
    "message": "This is a long looong test sentence,\nwith some big (biiiiig) words!",
}
```
**Successful Response:**
```json
HTTP/1.1 200 OK
Server: My RESTful API
Content-Type: application/json
Content-Length: xy

{
    "message": "\n—weird—\nThis is a long loonog test setcnene, with some big (biiiiig) wrods!\n—weird—\nsmoe wodrs tset lnog lonoog Tihs biiiiig seecntne wtih",
}
```
## Decode Message
**You send:**  Message to be decoded. 

**You get:** Decoded message.

**Request:**
```json
POST /v1/encode HTTP/1.1
Accept: application/json
Content-Type: application/json
Content-Length: xy

{
    "message": "\n—weird—\nThis is a long loonog test setcnene, with some big (biiiiig) wrods!\n—weird—\nsmoe wodrs tset lnog lonoog Tihs biiiiig seecntne wtih",
}
```
**Successful Response:**
```json
HTTP/1.1 200 OK
Server: My RESTful API
Content-Type: application/json
Content-Length: xy

{
    "message": "This is a long looong test sentence,\nwith some big (biiiiig) words!",
}
```

**Failed Response:**
```json
HTTP/1.1 400 Invald Request
Server: My RESTful API
Content-Type: application/json
Content-Length: xy

{
    "code": 400,
    "message": "Wrong number of seprators",
}