
from api import get_stock_stream

# Example usage

if __name__ == "__main__":
	params = {"max": 56069133} # Set the max ID for the Tweets, this max ID is not included
	ADBE_json = get_stock_stream('ADBE', params)
	#print(type(AAPL_json))
	#print(AAPL_json)
	
	with open('test2.txt', 'w') as f:
		
		for k, v in ADBE_json.items():
			if k == 'messages': # Find the messages with 'messages' as the key
				print('number of messages: ', len(v)) # v is a list
				for message_count in range(0,len(v)): # We will have 30 messages here by default. More details available at http://stocktwits.com/developers/docs/api#streams-symbol-docs
					f.write(str(v[message_count]))
					f.write("\n ############################### \n")
				

