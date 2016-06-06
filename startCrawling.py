
from api import get_stock_stream


if __name__ == "__main__":
	params = {"max": 56068528} # Set the max ID for the Tweets
	AAPL_json = get_stock_stream('AAPL', params)
	#print(type(AAPL_json))
	print(AAPL_json)
	with open('test.txt', 'w') as f:
