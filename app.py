from flask import Flask, request, render_template
import random

app = Flask(__name__)

roasts = [
    "Kayaknya {username} dibesarkan oleh netizen Twitter.",
    "@{username}? Kedengerannya kayak nama akun alter gagal.",
    "{username}? Auto skip.",
    "Kamu kayak WiFi gratisan: semua orang bisa pake, tapi bikin kesel.",
    "Senyummu bisa bikin bunga layu. Saking awkward-nya."
]

@app.route('/', methods=['GET', 'POST'])
def home():
    roast = None
    if request.method == 'POST':
        username = request.form['username'].strip('@ ')
        roast = random.choice(roasts).format(username=username)
    return render_template('index.html', roast=roast)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)