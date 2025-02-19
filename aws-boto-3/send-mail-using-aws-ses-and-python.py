
# attach created zip file to send
import boto3


source_email = "ciodev@celeritio.com"
destination_email = "prashant.mohite@celeritio.com"
messagebody = "testing SES aws"
subject = "AWS SES PART 1"



def send_mail():
    
    ses_client = boto3.client("ses" , region_name = "ap-south-1")
    
    CHARSET = "UTF-8"

    response = ses_client.send_email(
        Destination = {
            "ToAddresses":[
                destination_email,
            ]
        },
        Message = {
            "Body": {
                "Text" : {
                    "Charset" : CHARSET,
                    "Data" : messagebody,
                }
            },
            
            "Subject": {
            "Charset" : CHARSET,
            "Data" : subject,
            },
        },
        Source = source_email
    )