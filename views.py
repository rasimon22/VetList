from app import app
@app.route('/')
def index():
	return "<h1>This is the index</h1>"

