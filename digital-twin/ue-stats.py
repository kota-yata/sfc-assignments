import requests

def get_ue_stats(api_url, token, params):
  headers = {
    'Authorization': f'Bearer {token}'
  }
    
  try:
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return None
  
def generate_params(from_time, to_time, limit=10):
  return {
    'from': from_time,
    'to': to_time,
    'limit': limit
  }

api_url = 'https://n7wqz3y24a.execute-api.ap-northeast-1.amazonaws.com/v1/ues/gpsi-2151.external.5gc.mnc020.mcc440.3gppnetwork.org'
token = 'eyJraWQiOiI3VDNxeEFTdlY4aVd3aXlaYUtxZEVEbWJqbE9udDdGT3pyTmsxRXBtVUNzPSIsImFsZyI6IlJTMjU2In0.eyJjdXN0b206cmVzZWFyY2hfdG9waWMiOiLjg4njg63jg7zjg7MiLCJzdWIiOiIxOTBlYjdkYS1jMGVmLTRjNWEtODRmOS0wYTFkNmRlNWNmNWUiLCJjb2duaXRvOmdyb3VwcyI6WyJjb25zb3J0aXVtIl0sImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJjdXN0b206YXR0YWNoZWRfaW90X3BvbGljeSI6IjEiLCJjb2duaXRvOnByZWZlcnJlZF9yb2xlIjoiYXJuOmF3czppYW06OjIxMjQ1NTc1MzA1MTpyb2xlXC9hcC1ub3J0aGVhc3QtMV9rUld1aWc2b1YtY29uc29ydGl1bUdyb3VwUm9sZSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV9rUld1aWc2b1YiLCJjb2duaXRvOnVzZXJuYW1lIjoiMTkwZWI3ZGEtYzBlZi00YzVhLTg0ZjktMGExZDZkZTVjZjVlIiwib3JpZ2luX2p0aSI6IjNhZTU3MjI2LTU1ZjAtNDYwYi04MjJmLTFiZjQ4OWJkNmM5MyIsImNvZ25pdG86cm9sZXMiOlsiYXJuOmF3czppYW06OjIxMjQ1NTc1MzA1MTpyb2xlXC9hcC1ub3J0aGVhc3QtMV9rUld1aWc2b1YtY29uc29ydGl1bUdyb3VwUm9sZSJdLCJhdWQiOiIyamw4bTBxOTY4ZXVkajdsdWJwZGt1dnE5diIsImV2ZW50X2lkIjoiYjAzYWJjZTAtNjI5Zi00OTI2LWIwYmEtMmM2MTE4NDcxMWE4IiwiY3VzdG9tOnN1cGVydmlzb3IiOiJvc2FtdSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzQ3Mjk1OTAyLCJleHAiOjE3NTQ2Mzg1NzIsImlhdCI6MTc1NDYzNDk3MiwianRpIjoiZWM0OTFkODQtYzViZC00Y2UyLWIwNmItNWVmMzljMWUzNWU3IiwiZW1haWwiOiJ0MjM3NDZreUBzZmMua2Vpby5hYy5qcCJ9.grEEQWgp_uqvr06Ly8AEdppdKOadXQs9XMK0390Df9UApdLYfKutm9JDGNKmrLHSBs4-NQZGBdVaMqV53qmRNRqdC0BG2i9uY54xFUHo5zttuYWjHWHbY1BhLNLd6U04bbflSE2-RPOn-P70sijDsi5iM7YqVT9rw-URiI1gbjTMO93O8YxaXt9x3NunRNVE5iF5AKXlqj6_A1rKZCqvBaKE50hP57tiWyIZV_J5PoCTZdosVNaVXLvqbvXA1K5zPlafklWOOQfpiZIer_EYoXouh-JAFt56beLAjYnO68_atNFMX49mP1-meOlKUEDE-GF2x31reHC4cS9UH3PpiA'
param_from = '2025-08-08T15:30:00+09:00'
param_to = '2025-08-08T16:00:00+09:00'
stats = get_ue_stats(api_url, token, generate_params(param_from, param_to))
if stats:
  print("UE Stats:")
  for key, value in stats.items():
    print(f"{key}: {value}")
