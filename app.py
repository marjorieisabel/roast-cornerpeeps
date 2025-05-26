from flask import Flask, request, render_template
import random

app = Flask(__name__)

roasts = [
    "Kayaknya {username} dibesarkan oleh netizen X.",
    "Kamu, iya kamu {username} yang suka on tengah malem cuma buat scroll X. Mantengin timeline apa emang lagi nungguin ada yang ngucapin kamu good night baru tidur?",
    "{username}? Auto skip.",
    "Suka banget nge-like tweet, tapi ngapain? Emang udah jadi paparazzi digital?",
    "Update bio tiap minggu, tapi jati diri masih stuck di tweet 3 bulan lalu. Kamu kayak akun yang lagi coba cari vibe tapi malah keteteran, kayak charger yang sok kuat tapi cuma tahan 5 menit doang.",
    "Posting tweet vibes santai, tapi kenyataannya kamu lagi drama internal berat yang cuma bisa diungkap lewat emoji dan GIF random. Aku paham kok, tapi kalau kamu terus-terusan begitu, kapan happy-nya?",
    "Kamu yang doyan banget mention teman di tweet, padahal kadang temenmu cuma baca tanpa bales. Itu sama aja kayak ngirim undangan tapi yang dateng cuma kamu sendiri. Sedih, tapi lucu."
    "Eh kamu yang tiap malam ngabisin waktu scrolling X kayak lagi cari harta karun, tapi isinya cuma lihat orang lain makan atau nonton drama. Gak capek ya ngintip hidup orang lain tapi sendiri masih nganggur?",
    "Suka bikin akun baru, akhirnya ketauan juga karena vibes masih sama kayak sebelumnya. Mau punya berapa banyak akun lagi?",
    "Ngaku deh, kamu tuh cyber yang paling sering “online” tapi paling males bales chat. Followers kamu pasti nunggu jawaban kamu kayak nunggu update season baru drama Korea.",
    "Update-an kamu tuh sering kayak status galau yang cuma buat menarik perhatian. Padahal sih, followers juga pengen lihat kamu happy, bukan tambah bingung.",
    "Kalau kamu jadi charger, pasti charger KW yang kadang nyetrum, kadang gak nge-charge sama sekali. Followers kamu juga gitu, kadang aktif, kadang hilang entah kemana.",
    "Kamu tuh kayak spotlight di panggung kecil, bikin adem tapi gak pernah jadi bintang utama. Followers kamu? Mereka senang, tapi kadang pengen liat kamu lebih ngegas."
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
