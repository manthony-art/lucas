from flask import Flask, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
