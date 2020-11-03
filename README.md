# Weired-Text
Weirdtext translation service.

The is deployed on Heroku and can be accessed under this address: https://kkulczak-weird-text.herokuapp.com/

## Deployment
Deployment is performed automatically, after every push to `master` branch.
Commit have to pass all tests to be deployed. (Check github actions)

## Encryption mechanism
#### Encoding
For each original word in the original text, leave the first and last character of it in that
position, but shuffle (permutate) all the characters in the middle of the word. If possible,
the resulting “encoded” word MUST NOT be the same as the original word. Keep
everything else (whitespace, punctuation, etc.) like in the original. To make decoding by a
machine possible, your encoder shall also output a sorted list of original words (only
include words that got shuffled, not text that did not).
The composite output of the encoder (see example below) contains encoded text
(WeirdText) and also the sorted list of original words.
#### Decoding
For decoding composite text, first do a simple check whether the text looks like composite
output of your encoder. If not, raise some reasonable exception.
Then, use the encoded text and the words list to decode the text.
Your decoded output should, as far as possible, be identical to the original text. In case of
ambiguities (some encoded word could have been multiple original words), decoding
errors are acceptable.

ExampleOriginal Text (this is a single string formatted nicely for better viewing!)::
```
‘This is a long looong test sentence,\n’
‘with some big (biiiiig) words!’
```
Encoded Text (see comment above)::
```
‘\n—weird—\n’
‘Tihs is a lnog loonog tset sntceene,\n’
‘wtih smoe big (biiiiig) wdros!’
‘\n—weird—\n’
‘long looong sentence some test This with words’
```
Decoded Text::
```
‘This is a long looong test sentence,\n’
‘with some big (biiiiig) words!’
```



# API Documentation
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