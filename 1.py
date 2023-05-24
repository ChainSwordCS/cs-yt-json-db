# Python 3.7+

import json
#import argparse

#parser = argparse.ArgumentParser()
# parser.add_argument("option", help="hi")
#parser.add_argument("-i", help="hi")
#parser.add_argument("-a", help="add data from handmade JSON file")

#parser.parse_args()

#def parse_jsons_from_ytdl(folder):
# hi


newvid = {
	"title": "hello there my friend",
	"title_short": "Big Brother☆", # optional
	"manually_checked": True,
	"filename": "big_brother", # partial filename. please keep it ASCII-compatible, and prefer no spaces


	# if the Title had part or all of itself translated by me, make a note. provide the original, un-translated title(s) below.
	"title_translated": False,

	# optional
	"title_og": "Big Brother☆",
	"title_og_lang": "en",

	# author / uploader. this is an id that corresponds to an entry in db2. (is a string)
	# "author_id": "0",
	"author_name": "nisusansu",

	# video uploads
	"uploads": [
		{
			"id": "sm33175756",
			"site": "nico",
			"upload_date": 0,
			"title": "Big Brother☆",
			"desc": "h",
			"user_id": "0"
		}
	],

	# fuck
	"sus": True
}

newdata = {
	"vids": [
		{
			"title": "Big Brother☆",
			"title_short": "Big Brother☆", # optional
			"manually_checked": True,
			"filename": "big_brother", # partial filename. please keep it ASCII-compatible, and prefer no spaces


			# if the Title had part or all of itself translated by me, make a note. provide the original, un-translated title(s) below.
			"title_translated": False,

			# optional
			"title_og": "Big Brother☆",
			"title_og_lang": "en",

			# author / uploader. this is an id that corresponds to an entry in db2. (is a string)
			# "author_id": "0",
			"author_name": "nisusansu",

			# video uploads
			"uploads": [
				{
					"id": "sm33175756",
					"site": "nico",
					"upload_date": 0,
					"title": "Big Brother☆",
					"desc": "h",
					"user_id": "0"
				}
			],

			# fuck
			"sus": True
		}
	]
}


#with open("db1.json", "r+") as db1:
#	data = json.load(db1)
#	data["vids"].append(json.dumps(newvid))




#with open("db1.json") as db1_read:
#	data = json.load(db1_read)

#data.update(newdata)

#with open("db1.json", "w") as db1_write:
#	json.dump(data, db1_write)
