from requests import get

def send_sms(phone, message):
    username = ''
    password = ''
    msg = message
    _from = '+'
    to = phone
    url = f"(url)={_from}&to={to}&msg={msg}&uname={username}&pass={password}"
    result = get(url)
    return "ارسال شد"