from flask import Flask #we import the flask class
from flask import url_for

app = Flask(__name__) #our app is an instance of the
#Flask Class and we say the name is __name__
#aka the name of this file





#below is a decorator, says what url this functon is displayed at
#decorators are pretty much modify the function when you call them,
# so maybe do smthn before or after or use a var to
# determine smthn
@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"


#@app.route("/<var_name>") causes function to receive var_name as argument if ask for it
#can also specify what type for example int:<> path:<>, string:<>, float:<>, uuid:<>
@app.route("/hello/<name>/")
def hello(name):
	return f"Hello {name}" #fstring where inside {} you can use vars and normal python


#when path is /path/ then you can access with both /path/ and /path
# but when /path then only /path will access

#rather than statically typing urls aka /user/<username>/
#what if wanted to get dynamic ones, thats what url_for() is
# do url_for("function_name", other parameters like next or values for username or etc)

if __name__ == "__main__": #if we run file directly only then start app
	app.run()
	# if you wannna make it available externally then
	#do app.run(host="0.0.0.0")
