



point:

main.py

function name equals deploy xxx
or need to specify the --end_point


deploy:

gcloud beta functions deploy hello_http --runtime python37 --trigger-http


trigger:


curl -X POST https://us-central1-yh48-214406.cloudfunctions.net/hello_http  -H "Content-Type:application/json" --data '{"name":"Keyboard Cat"}'
