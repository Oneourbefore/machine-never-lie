import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = 'dabfc7328505d31e6e5f7669fb7b0af0'
redirect_uri = 'https://example.com/oauth'
code = 'rTbAaDJdv2oDzWLTCqA_7AKbPK2ALwUCdgbFPlHBmnXom-crng_E08ftEkh8HgRDQoqQKgopcJ4AAAGC5NJyuA'

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)
