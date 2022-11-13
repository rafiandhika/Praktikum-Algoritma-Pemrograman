import requests
import json
import os
import shutil

url = "https://hooks.slack.com/services/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"

file1 = '/home/infosec/NYP/OnionSearch/kredivo/nyobain1.txt'
file2 = '/home/infosec/NYP/OnionSearch/kredivo/nyobain2.txt'

f = open('/home/infosec/NYP/OnionSearch/kredivo/nyobain3.txt','r')


def overwrite():
	root_src_dir = '/home/infosec/NYP/OnionSearch/kredivo/nyobain1.txt'
	root_dst_dir = '/home/infosec/NYP/OnionSearch/kredivo/nyobain2.txt'

	for src_dir, dirs, files in os.walk(root_src_dir):
    		dst_dir = src_dir.replace(root_src_dir,root_dst_dir,1)
    		if not os.path.exists(dst_dir):
        		os.makedirs(dst_dir)
    		for file_ in files:
        		src_file = os.path.join(src_dir, file_)
        		dst_file = os.path.join(dst_dir, file_)
        		if os.path.exists(dst_file):
            			# in case of the src and dst are the same file
            			if os.path.samefile(src_file, dst_file):
                			continue
            			os.remove(dst_file)
        		shutil.move(src_file, dst_dir)

def compare(file1,file2):
	with open(file1,'r') as f:
		d=set(f.readlines())
	with open(file2,'r') as f:
		e=set(f.readlines())

	open('/home/infosec/NYP/OnionSearch/kredivo/nyobain3.txt','w').close() #Create the file

	with open('/home/infosec/NYP/OnionSearch/kredivo/nyobain3.txt','a') as f:
		for line in list(d-e):
			f.write(line)

def sendslack():
	for x in f.readlines():
		y = x.replace('"','').split(',')
		payload = json.dumps({
			"attachments": [
				{
					"color": "#f2c744",
					"blocks": [
						{
							"type": "divider"
						},
						{
							"type": "section",
							"text": {
								"type": "mrkdwn",
								"text": ":clipboard: *KREDIVO on .onion search engine* :eyes:"
							}
						},
						{
							"type": "divider"
						},
						{
							"type": "section",
							"text": {
								"type": "mrkdwn",
								"text": y[1]
							}
						},
						{
							"type": "section",
							"text": {
								"type": "mrkdwn",
								"text": y[2]
							}
						}
					]
				}
			]
		})
		headers = {
  		'Content-type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)

		print(response.text)

compare()
overwrite()
sendslack()
