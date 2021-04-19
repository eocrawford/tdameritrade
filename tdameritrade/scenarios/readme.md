Swagger for getting JWT:

Get initial auth code (decode URL at https://www.urldecoder.org/ before submitting auth code)
https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=http://localhost:8080&client_id=TDAMERITRADE_CLIENT_ID%40AMER.OAUTHAP

Use auth token to get access and refresh tokens:
https://developer.tdameritrade.com/authentication/apis/post/token-0

Reference:
https://developer.tdameritrade.com/content/getting-started
https://developer.tdameritrade.com/content/authentication-faq

