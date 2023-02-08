import boto3

s3 = boto3.client("s3")

s3.upload_file(
	Filename= "/Users/hemantkumarboddikura/Documents/fileupload/random.txt",
	Bucket = 'test1234567891234567',
	Key = "UPloaded by doomsday"
)

