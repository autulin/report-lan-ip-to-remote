# report-lan-ip-to-remote
report local ip to remote server/mail

# Usage

Edit config in `report-client.py`

```python
url = "http://your-server/ip"

### edit your SMTP email config
smtpserver = "smtp.xxx.com"
username = "your username"
password = "your password"
sender = "user@xxx.com"
receiver = ["receiver@xxx.com"]
subject = "edit your email subject"
```

Compile(using maven) or [download](https://github.com/autulin/report-lan-ip-to-remote/releases/tag/1.0) the server jar

Run `report-client.py` in which machine you want to report its ip.
```shell
python3 report-client.py
```

Run the jar in remote server
```shell
java -jar -Dserver.port=8088 report-lan-ip-to-remote-0.0.1-SNAPSHOT.jar
```

then you can get ip from the url `http://your-server/ip`
