file = open('/Users/vidursingh/Desktop/python/File_management_app/sample.txt','r')
content = file.read()
file.close()
print(f"Content of 'sample.txt': {content}")