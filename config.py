
port = 2000

projects = {
    'development': ['flappy_parrot'],
    'production': []
    }

imageRoot = {
    'development': 'http://localhost:2000/resources/',
    'production': 'https://s3-eu-west-1.amazonaws.com/turing-resources/'
    }

mongolabUri = {
    'development': 'mongodb://localhost:27017/turing_development',
    'production': 'mongodb://heroku_dh1386kx:5ki9curvtt1r4bsunu3893k3rh@ds033754.mongolab.com:33754/heroku_dh1386kx'
    }
