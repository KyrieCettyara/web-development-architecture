# Introduction to Web Architecture
# Background
Platform jejaring sosial sederhana yang mirip dengan twitter namun hanya berfokus pada pengalaman pengguna yang lebih sederhanan dan intuitif.


## Program Description 
1. User dapat melakukan registrasi agar terdaftar sebagai pengguna.
2. User dapat melakukan login untuk masuk ke dalam sistem.
3. User yang berhasil melakukan login dapat menambahkan tweet.
4. User yang berhasil melakukan login dapat menguplod gambar.
5. User yang berhasil melakukan login dapat melihat leaderboar.


# User Flowchart
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/flow.png)

Berdasarkan flow diatas. Pertama kali user akan melihat halaman login. User yang belum memiliki akun diharuskan untuk melakukan registrasi terlebih dahulu. Jika user sudah memiliki akun, user dapat memasukkan username dan password. Jika username dan password yang diberikan benar maka akan ditampilkan halaman home. Jika username dan password yang dimasukkan salah maka user akan diminta untuk memasukkan kombinasi username dan password yang benar. User yang sudah berhasil mengakses halaman home dapat membuat tweet dengan mengupload gambar ataupun tidak. Melalui halaman home user juga dapat melihat tweet yang dimasukkan oleh user lainnya dan mengakses leaderboard untuk melihat jumlah banyak tweet yang diinput oleh semua user. 


# Requirements and Technology Used
### backend
- Python
- Flask
- Flask-JWT-Extended
- Flask-Cors
- Flask-SQLAlchemy
- psycopg2

### frontend
- vue
- vue-router
- axios
- datatables.net
- tailwindcss
- vue-sweetalert2
- pinia



### Login Page
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/login.png)


### Home Page
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/home.png)

### Upload Gambar
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/upload.png)

![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/upload_image.png)

![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/upload_image2.png)

Untuk menyimpan gambar digunakan minio yang disetup sebagai berikut
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/minio.png)


### Leaderboard
![alt text](https://github.com/KyrieCettyara/web-development-architecture/blob/main/image/leaderboard.png)










