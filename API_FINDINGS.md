# API Findings: JSONPlaceholder

Testers (pair): <name 1>, <name 2>
Date: <date>

Record what the server actually returned for each route. A value
copied from the documentation without being checked against a real
request is not a finding.


### GET /posts/1

| Field | Value |
|---|---|
| Status code | 200 |
| Content-Type | application/json; charset=utf-8 |

Response body keys and their types:

| Key | Type | Example value |
|---|---|---|
| userId | int | 1 |
| id | int | 1 |
| title | str | sunt aut facere repellat provident occaecati excepturi optio reprehenderit |
| body | str | quia et suscipit... |



### GET /posts

| Field | Value |
|---|---|
| Status code | 200 |
| Content-Type | application/json; charset=utf-8 |
| Response body type | JSON array (list) |
| Number of items | 100 |
| Item type | JSON object |

Response body keys and their types:

| Key | Type | Example value |
|---|---|---|
| userId | int | 1 |
| id | int | 1 |
| title | str | sunt aut facere repellat provident occaecati excepturi optio reprehenderit |
| body | str | quia et suscipit... |



### POST /posts

| Field | Value |
|---|---|
| Status code | 201 |
| Content-Type | application/json; charset=utf-8 |

Request body sent:

```json
{
  "title": "Lab 6 API Test",
  "body": "Testing POST request",
  "userId": 1
}
```

Response body keys and their types:

| Key | Type | Example value |
|---|---|---|
| title | str | Lab 6 API Test |
| body | str | Testing POST request |
| userId | int | 1 |
| id | int | 101 |



### DELETE /posts/1

| Field | Value |
|---|---|
| Status code | 200 |
| Content-Type | application/json; charset=utf-8 |
| Response body | {} |


## Notes

Record here any disagreement between the published guide and the
server's actual response, including any route where the server
appears to accept the request without performing the operation it
describes.
