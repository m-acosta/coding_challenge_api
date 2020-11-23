# coding_challenge_api
# FarApp Software Engineer Candidate Coding Challenge

### Introduction and Instructions
    <!-- 
    1 Pull 1000 names from some public API either in front-end code or back-end. A couple possibilities would
    be Facebook's Graph API (https://developers.facebook.com/docs/graph-api/reference) and LinkedIn's
    API (https://developer.linkedin.com/docs/rest-api). If you are unfamiliar with OAUTH it’s recommended
    you skip these options and seek an API that does not require it such as https://randomuser.me/
    2 Store the results from step 1 locally (we suggest a SQLite database, but you can use any format you'd
    like). This should be run on the back-end (i.e. imagine this is running on a server where we need the data
    on a database on the server).
    3 Develop a simple webpage that will display 100 names in a table (out of 1000).
    4 Add email and phone columns to the webpage table. Then, provide a button for each table entry that
    allows you to manually enter a phone and/or email address. Add some basic validation for the phone
    and/or email address (e.g. '123' would be rejected as a phone number). Validation can be run on either
    front-end or back-end. The data should be stored in storage you set up in step 2.
    5 Add buttons that allow you to sort the table by name or email address.
    6 Add a search function to the table.
    7 Add a button that allows you to export the table data to a .csv download file. The .csv file should reflect
    the current status of the table (including sort order and search results). 
    -->

### Usage

```json
[
    {
        "name": "Name of user from https://randomuser.me/",
        "email": "Email attached to the user's name that will be enterred manually",
        "phone": "Phone number attached to the user's name that will be enterred manually"
    }
]
```

### List 100 in a table (out of 1000)

**Definition**

`GET /users`

**Response**

- `200 OK` on success

### Add email and phone fields to a user

**Definition**

`POST /user`

**Arguments**

- `"phone":string` a valid phone number in the format 1234567890
- `"email":string` a valid email address in the format foo@mail.com

**Response**

- `201 Created` on success