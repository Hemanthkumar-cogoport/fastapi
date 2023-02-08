import boto3
s3 = boto3.resource('s3')
BUCKET = "test1234567891234567"
s3.Bucket(BUCKET).upload_file("/Users/hemantkumarboddikura/Documents/fileupload/index.html", "dump/file")