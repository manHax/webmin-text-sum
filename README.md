# Meringkas Teks menggunakan text rank

### Crawling text
data yang digunakan pada percobaan ini adalah hasil crawling menggunakan library **scrapy python** [folder news](https://github.com/manHax/webmin-text-sum/tree/main/news).

### Pra proses text
dari data hasil crawling tersebut dilakukan pra-proses untuk menghilangkan karakter-karakter yang tidak diperlukan, emoticon dan sumber berita (dalam kasus ini saya menghilangkan kata `jawapos.com` pada paragraph).

### Melakukan tokenisasi
tokenisasi dilakukan menggunakan library `nltk` yang dimaksudkan untuk membuat list kalimat
([cell 8-9](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))

### Menghitung vektorisasi
vektorisasi dilakukan menggunakan library `sklearn` pada list kalimat yang telah terbentuk dari proses tokenisasi ([cell 10](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))

### Normalisasi (hitung Tfidf)
dari hasil vektorisasi dilakukan normalisasi menggunakan library `sklearn` dengan menghitung Tfidf dari matrix hasil vektorisasi ([cell 12](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))

### Menghitung matrix kedekatan (matrix adjacency)
matrix adjacency didapat dengan mengalikan matrix normal dengan matrix normal transpose ([cell 17](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))

### Membuat graph
matrix adjacency yang telah terbentuk dibuatkan sebuah graph menggunakan library `networkx` untuk melihat hubungan antar kalimat pada list kalimat.

### Menghitung Pagerank
dengan menggunakan library `networkx` pagerank dibentuk dari matrix adjacency. ([cell 21](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))

### Menampilkan informasi 
* array kalimat ([cell 23](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))
* nilai min dan max ([cell 23](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))

### Summary text
* membuat nilai batas yang didapat dengan menggunakan rumus `min-max normalization` yang selanjutnya dijumlahkan dan dibagi dengan jumlah kalimat. `thresehold = (sum(minmax value) / len(minmax value))` ([cell 26-27](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))
* menyeleksi kalimat yang mempunyai nilai diatas batas yang telah ditentukan ([cell 28](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))
* menjadikan kalimat dalam bentuk paragraph ([cell 29](https://github.com/manHax/webmin-text-sum/blob/main/Mengestrak__ringkasan.ipynb))
