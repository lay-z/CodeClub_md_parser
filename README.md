#TuringLab Content Curator

The TuringLab content curator is used to obtain content for TuringLab
cards system.


#AWS Policy 

Allows full write access to turing-resources

```json
{
    "Version": "2012-10-17",
    "Statement": [
    {
        "Action": "s3:*",
        "Effect": "Allow",
        "Resource": [
        "arn:aws:s3:::turing-resources",
        "arn:aws:s3:::turing-resources/*"
        ]
    }
    ]
}
```

Allows read access to bucket lists

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "arn:aws:s3:::*"
        }
    ]
}
```