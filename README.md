# Instagram-API-python
Python script to retrieve Instagram photos queried by location or tags. Sqlite database used for continuation.

Libraries used:
- Requests
http://docs.python-requests.org/en/latest/
- geolocation-python
https://pypi.python.org/pypi/geolocation-python/0.2.0
- sqlite3

Authentication:
Client ID and Client Secret are provided by Instagram on registering the client. These client details are first used to get an access token generated on-demand by Instagram. This access token is then used to make API calls.

Usage:
'geolocation-python' library is used to get the coordinates of the queried location. These coordinates are then plugged into the media search API call provided by Instagram. Data returned is in JSON format. Image urls are extracted and the binary response of each HTTP request is saved as a .jpg file.
