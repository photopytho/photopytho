// Daftar nama gambar dalam folder gallery
const images = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg',
    'image6.jpg',
    'image7.jpg',

    // Tambahkan nama-nama gambar lainnya sesuai dengan koleksi Anda
];

// Fungsi untuk mengambil gambar secara acak dari array
function getRandomImage(imagesArray) {
    const randomIndex = Math.floor(Math.random() * imagesArray.length);
    return imagesArray[randomIndex];
}

// Fungsi untuk menampilkan gambar dalam elemen gallery
function displayRandomImage() {
    const galleryElement = document.getElementById('gallery');
    const randomImage = getRandomImage(images);
    const imageElement = document.createElement('img');
    imageElement.src = 'gallery/' + randomImage; // Path ke folder gallery
    galleryElement.innerHTML = ''; // Kosongkan elemen gallery sebelum menambahkan gambar baru
    galleryElement.appendChild(imageElement);
}

// Tampilkan gambar pertama saat halaman dimuat
displayRandomImage();

// Tampilkan gambar baru setiap beberapa detik (misalnya, setiap 5 detik)
setInterval(displayRandomImage, 5000); // Ubah angka ini sesuai dengan interval yang Anda inginkan (dalam milidetik)
