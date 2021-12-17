# File Upload

On the home website, you can scroll down to find a `upload image` link.

![alt text](img/upload.png "Upload")

![alt text](img/upload_file.png "Upload file")

Uploading a random file gives us an error
```
Your image was not uploaded.
```

![alt text](img/error.png "Error on Upload Page")

We interupt the request with `BurpSuite` :

![alt text](img/bp1.png "BurpSuite 1")

We send it to the repeater, notice that the content type is a php file :
```
Content-Type: text/php
```

Let's change that to `image/jpeg` and send the request :


![alt text](img/bp_2.png "BurpSuite 2")

Voila we get the flag.

## How to protect ?
Make a script the checks the extention, and check content type. Maybe also restrict the upload only to admins.