let selectedPDF = null;

function handleFileSelect() {
    const fileInput = document.getElementById('pdfInput');
    const selectedPDFName = document.getElementById('selectedPDFName');
    if (fileInput.files.length > 0) {
        selectedPDF = fileInput.files[0];
        selectedPDFName.textContent = selectedPDF.name;
    } else {
        selectedPDF = null;
        selectedPDFName.textContent = '';
    }
}

function submitData() {
    const ageRange = document.getElementById("ageRange").value;
    const bookList = document.getElementById("bookList");

    if (selectedPDF && ageRange) {
        const newRow = document.createElement("tr");

        const bookCell = document.createElement("td");
        bookCell.textContent = selectedPDF.name;
        newRow.appendChild(bookCell);

        const ageCell = document.createElement("td");
        ageCell.textContent = ageRange;
        newRow.appendChild(ageCell);

        const deleteCell = document.createElement("td");
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Sil";
        deleteButton.className = "delete-btn";
        deleteButton.onclick = function() {
            bookList.removeChild(newRow);
        };
        deleteCell.appendChild(deleteButton);
        newRow.appendChild(deleteCell);

        bookList.appendChild(newRow);

        document.getElementById("pdfInput").value = "";
        document.getElementById("ageRange").value = "";
        document.getElementById("selectedPDFName").textContent = '';
        selectedPDF = null;
    } else {
        alert("Lütfen bir PDF dosyası yükleyin ve yaş aralığını girin!");
    }
}

function uploadData() {
    const bookList = document.getElementById("bookList");
    const rows = bookList.getElementsByTagName("tr");
    if (rows.length > 0) {
        bookList.innerHTML = '';
        alert("Veri setine yüklendi!");
    } else {
        alert("Yüklemeniz gereken kitap bulunmuyor.");
    }
}
