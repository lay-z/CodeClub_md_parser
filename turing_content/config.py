
port = 2000

aws = {
    'region_name': 'eu-west-1',
    'aws_access_key_id': 'AKIAIRNBRPBJGFKX5S2Q',
    'aws_secret_access_key': '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'
}

bucketName = 'turing-resources'

turingResources = {
    'development': 'http://localhost:2000/resources/',
    'production': 'https://s3-eu-west-1.amazonaws.com/{}/'.format(bucketName)
}

mongolabUri = {
    'development': 'mongodb://localhost:27017/turing_development',
    'production': 'mongodb://heroku_dh1386kx:5ki9curvtt1r4bsunu3893k3rh@ds033754.mongolab.com:33754/heroku_dh1386kx'
}

pythonMongolabUri = {
    'development': 'mongodb://localhost/codechallenge-dev',
    'production':  'mongodb://heroku_lkt4dnd4:o4d3h5kpbq8e49psnk6m24o00q@ds055872.mongolab.com:55872/heroku_lkt4dnd4'
}