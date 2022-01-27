function previewImage() {
    const file = document.getElementById("file").files;
    if (file.length > 0) {
        const fileReader = new FileReader();

        fileReader.onload = function (event) {
            const img = document.getElementById('preview')
            img.style.display = 'block'
            img.setAttribute("src", event.target.result);
        };

        fileReader.readAsDataURL(file[0]);
    }
}