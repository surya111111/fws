from flask import Flask, request
app = Flask(__name__)

people = {
    'klong':{
        'name': 'Kevin',
        'age': 52,
        'passwd' : 'simple'
    },
    'sprakash': {
        'name': 'Surya',
        'age': 26,
        'passwd': 'complex'
    }
}

@app.route('/login/', methods=['POST'])
def login():

    # GET USER TABLE VIA SELECT
    username = request.values.get('username')
    passwd = request.values.get('passwd')


    sql = "SELECT from users where username = '" + username + "';"


    if not username in people:
        return "ERROR"
    if not people[username]["passwd"] == passwd:
        return "ERROR"
    return people[username]["name"]

@app.route('/data/')
def data():
    output = "["
    count = 0
    #
    # for person in people:
    #     if count > 0:
    #         output = output + ','
    #     count = count + 1
    #     output = output + '{"name":"' + person["name"] + '"}'

    output = output + "]"
    return output


@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color:#4B0082;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

/* Extra styles for the cancel button */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color:#4B0082;
}

/* Center the image and position the close button */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
  position: relative;
}

img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

</style>
</head>
<body>
    Home Page
    <form action="/login/" method="POST">
    <input name="username" placeholder="User Name">
    <input name="passwd" placeholder="Password" type="password">    
    <button type="submit"> Login </button>
    </form>
    <script>
    /*
    fetch('/data/')
  .then((response) => {
    return response.json();
  })
  .then((myJson) => {
    console.log(myJson);
    for(var i = 0; i < myJson.length; i++){
        var b = document.createElement("button");
        b.innerHTML = myJson[i].name;
        document.body.append( b );
    }
  });
  */
    </script>
</body>
</html>
    '''
    # return '''
    # <a href="/data/">
    # GO to Data
    # </a>
    # '''

if __name__ == '__main__':
    app.run()
