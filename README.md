Fish Length to Weight Lookup Service
==============================================

An extremely simple fish length to weight lookup service with
limited features and very sadly-incomplete species coverage.

Utilizes data from:
https://www.dnr.state.mn.us/fishing/regs.html
https://dnr.wi.gov/topic/fishing/questions/estfishweight.html
https://www.iowadnr.gov/Portals/idnr/uploads/fish/regs_fish.pdf
http://www.swmnhunting.com/6783-2/
https://gf.nd.gov/fishing/regulations-guide
https://www.dec.ny.gov/outdoor/9222.html
... along with some linear interpolation to fill gaps


Requirements
------------

Python 3.6


Usage
-----

Weight lookup functionality is also self-contained in:

'''
fishweight.fishweight.lengthToWeight(species, length)
'''

Accepts lengths in quarter-inch increments

Returns JSON in the format:
'''
{
    "Species": "Walleye",
    "Length": "23.75",
    "MN DNR Table": 5.225,
    "Catch & Release Forumlas (WI and IA DNR)": 4.962,
    "ND DNR Table": 4.95,
    "NY DEC Table": 4.531,
    "average": 4.917
}
'''
... which includes the input species and length along with values 
from each lookup table (if present) and an average value across 
all tables with a value

Deploy as AWS Lambda
--------------------

For running as an AWS Lambda function, utilize index.handler

Also included is template.yml and buildspec.yml for use in 
AWS CodeStar with AWS SAM (Serverless Application Model)

More info:
http://docs.aws.amazon.com/codestar/latest/userguide/welcome.html
https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md
http://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html
https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html
