import requests

url = "http://192.168.1.144/index.php"
data = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

response = requests.post(url, data=data, headers={"Content-Type": "text/plain"})
print("Status Code:", response.status_code)
print("Response Body:", response.text)


