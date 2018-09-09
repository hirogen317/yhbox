
# Readme

Helloworld / cloud sql collection for gcp



point:


- main.py

- function name equals deploy xxx
- or need to specify the --end_point


**deploy**

```
gcloud beta functions deploy hello_http --runtime python37 --trigger-http
```

trigger:

```
curl -X POST url/function_name  -H "Content-Type:application/json" --data '{"name":"Keyboard Cat"}'
```
