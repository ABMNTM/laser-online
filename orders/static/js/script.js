function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section.style.display === 'none') {
        section.style.display = 'flex';
    }
    section.scrollIntoView({ behavior: 'smooth' });
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

window.onclick = function (event) {
    const aboutModal = document.getElementById('aboutModal');
    const serviceModal = document.getElementById('serviceModal');
    const thicknessModal = document.getElementById('thicknessModal');
    const materialModal = document.getElementById('materialModal');
    if (event.target === aboutModal) {
        closeModal('aboutModal');
    }
    if (event.target === serviceModal) {
        closeModal('serviceModal');
    }
    if (event.target === thicknessModal) {
        closeModal('thicknessModal');
    }
    if (event.target === materialModal) {
        closeModal('materialModal');
    }
};

let selectedMaterial = null;
let selectedThickness = null;
let selectedFile = null;

const materialThicknessMap = {
    'Iron Sheet': [1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 10, 12, 15, 20],
    'Galvanized Sheet': [0.3, 0.4, 0.5, 0.8, 1.0, 1.5, 2, 2.5],
    'Stainless Steel Sheet': [0.3, 0.4, 0.5, 0.8, 1.0, 1.5, 2],
    'Aluminum Sheet': [0.35, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 10],
    'Brass Sheet': [1, 2, 3, 4, 5, 6],
    'Copper Sheet': [0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.5, 2],
    'Plexiglass - Clear (Transparent)': [1, 2, 3, 4, 5, 6, 8, 10],
    'Plexiglass - Colored (Opaque/Transparent)': [2, 3, 4, 5, 6],
    'Plexiglass - Frosted (Matte/Opaque)': [2, 3, 4, 5],
    'Plexiglass - Fluorescent (Phosphorescent)': [2, 3, 4],
    'Plexiglass - Mirror Effect (Acrylic Mirror)': [2, 3],
    'Plexiglass - Impact Resistant (Hard/Unbreakable)': [3, 4, 5, 8, 10],
    'Plexiglass - Multi-Style (Reflective Sheet)': [1, 1.5, 2],
    'Plexiglass - Patterned/Rippled/Light-Edge': [2, 3]
};

function openMaterialModal(type) {
    const materialSelect = document.getElementById('materialSelect');
    materialSelect.innerHTML = '<option value="" disabled selected>Select a material</option>';
    
    const materials = type === 'metal' ? 
        ['Iron Sheet', 'Galvanized Sheet', 'Stainless Steel Sheet', 'Aluminum Sheet', 'Brass Sheet', 'Copper Sheet'] :
        ['Plexiglass - Clear (Transparent)', 'Plexiglass - Colored (Opaque/Transparent)', 
         'Plexiglass - Frosted (Matte/Opaque)', 'Plexiglass - Fluorescent (Phosphorescent)', 
         'Plexiglass - Mirror Effect (Acrylic Mirror)', 'Plexiglass - Impact Resistant (Hard/Unbreakable)', 
         'Plexiglass - Multi-Style (Reflective Sheet)', 'Plexiglass - Patterned/Rippled/Light-Edge'];

    materials.forEach(material => {
        const option = document.createElement('option');
        option.value = material;
        option.textContent = material;
        materialSelect.appendChild(option);
    });

    openModal('materialModal');
}

function confirmMaterial() {
    const materialSelect = document.getElementById('materialSelect');
    selectedMaterial = materialSelect.value;

    if (!selectedMaterial) {
        materialSelect.style.border = '2px solid red';
        return;
    }

    const thicknessSelect = document.getElementById('thicknessSelect');
    thicknessSelect.innerHTML = '<option value="" disabled selected>Select thickness (mm)</option>';
    
    const thicknesses = materialThicknessMap[selectedMaterial] || [];
    thicknesses.forEach(thickness => {
        const option = document.createElement('option');
        option.value = thickness;
        option.textContent = `${thickness} mm`;
        thicknessSelect.appendChild(option);
    });

    closeModal('materialModal');
    materialSelect.value = '';
    openModal('thicknessModal');
}

function confirmThickness() {
    const thicknessSelect = document.getElementById('thicknessSelect');
    selectedThickness = thicknessSelect.value;

    if (!selectedThickness) {
        thicknessSelect.style.border = '2px solid red';
        return;
    }

    const summary = document.getElementById('materialSummary');
    summary.innerHTML = `Selected Material: ${selectedMaterial}, Thickness: ${selectedThickness} mm <button class="change-selection-btn" onclick="resetMaterialSelection()">Change Selection</button>`;

    const confirmBtn = document.getElementById('confirmMaterialBtn');
    confirmBtn.disabled = false;

    document.getElementById('materialInput').value = selectedMaterial;
    document.getElementById('thicknessInput').value = selectedThickness;

    closeModal('thicknessModal');
    thicknessSelect.value = '';
}

function resetMaterialSelection() {
    selectedMaterial = null;
    selectedThickness = null;

    const summary = document.getElementById('materialSummary');
    summary.textContent = 'Please select a material and thickness.';
    const confirmBtn = document.getElementById('confirmMaterialBtn');
    confirmBtn.disabled = true;

    document.getElementById('materialInput').value = '';
    document.getElementById('thicknessInput').value = '';
}

function validateAndScroll() {
    const fullName = document.getElementById('full-name');
    const mobile = document.getElementById('mobile');
    const email = document.getElementById('email');
    const address = document.getElementById('address');

    fullName.classList.remove('invalid');
    mobile.classList.remove('invalid');
    email.classList.remove('invalid');
    address.classList.remove('invalid');

    let isValid = true;
    let errorMessage = '';

    if (!fullName.value.trim()) {
        fullName.classList.add('invalid');
        isValid = false;
        errorMessage += 'Full name is required.\n';
    }

    if (!mobile.value.trim()) {
        mobile.classList.add('invalid');
        isValid = false;
        errorMessage += 'Mobile number is required.\n';
    } else {
        const mobilePattern = /^09\d{9}$/;
        if (!mobilePattern.test(mobile.value)) {
            mobile.classList.add('invalid');
            isValid = false;
            errorMessage += 'Mobile number must start with "09" and be exactly 11 digits (e.g., 09123456789). No spaces or other characters allowed.\n';
        }
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.value.trim()) {
        email.classList.add('invalid');
        isValid = false;
        errorMessage += 'Email is required.\n';
    } else if (!emailPattern.test(email.value)) {
        email.classList.add('invalid');
        isValid = false;
        errorMessage += 'Please enter a valid email address (e.g., user@example.com).\n';
    }

    if (!address.value.trim()) {
        address.classList.add('invalid');
        isValid = false;
        errorMessage += 'Address is required.\n';
    }

    if (!isValid) {
        alert(errorMessage);
        return;
    }

    scrollToSection('upload');
}

// Real-time mobile input validation
document.addEventListener('DOMContentLoaded', () => {
    const mobileInput = document.getElementById('mobile');
    mobileInput.addEventListener('input', () => {
        const mobilePattern = /^09\d{0,9}$/;
        if (mobileInput.value && !mobilePattern.test(mobileInput.value)) {
            mobileInput.classList.add('invalid');
        } else {
            mobileInput.classList.remove('invalid');
        }
    });
});

function handleUploadButtonClick() {
    const fileInput = document.getElementById('fileInput');
    const uploadBtn = document.getElementById('uploadBtn');
    const fileNameDisplay = document.getElementById('fileName');
    const uploadBox = document.getElementById('uploadBox');

    if (uploadBtn.classList.contains('remove')) {
        fileInput.value = '';
        selectedFile = null;
        fileNameDisplay.textContent = '';
        uploadBtn.textContent = 'Choose File';
        uploadBtn.classList.remove('remove');
        uploadBox.classList.remove('invalid');
    } else {
        fileInput.click();
    }

    fileInput.onchange = function () {
        if (fileInput.files.length > 0) {
            selectedFile = fileInput.files[0];
            fileNameDisplay.textContent = selectedFile.name;
            uploadBtn.textContent = 'Remove & Upload Again';
            uploadBtn.classList.add('remove');
            uploadBox.classList.remove('invalid');
        }
    };
}

const uploadBox = document.getElementById('uploadBox');
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('dragover');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('dragover');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        const fileInput = document.getElementById('fileInput');
        fileInput.files = files;
        selectedFile = files[0];
        const fileNameDisplay = document.getElementById('fileName');
        fileNameDisplay.textContent = selectedFile.name;
        const uploadBtn = document.getElementById('uploadBtn');
        uploadBtn.textContent = 'Remove & Upload Again';
        uploadBtn.classList.add('remove');
        uploadBox.classList.remove('invalid');
    }
});

function validateUploadAndScroll() {
    const uploadBox = document.getElementById('uploadBox');
    if (!selectedFile) {
        uploadBox.classList.add('invalid');
        alert('Please upload a CNC file.');
        return;
    }
    scrollToSection('material-selection');
}

function submitOrderForm() {
    if (!selectedMaterial || !selectedThickness || !selectedFile) {
        alert('Please complete all steps: enter details, upload file, and select material/thickness.');
        return;
    }

    const form = document.getElementById('orderForm');
    const formData = new FormData(form);
    formData.append('cnc_file', selectedFile);

    // Log form data for debugging
    console.log('Form Data Sent:');
    for (let pair of formData.entries()) {
        console.log(pair[0] + ': ' + (pair[1] instanceof File ? pair[1].name : pair[1]));
    }

    fetch('/submit_order/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => {
        console.log('Server Response Status:', response.status);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Server Response Data:', data);
        if (data.success) {
            alert(`Order submitted! Your Receipt Code is ${data.receipt_code}. Please save this code to track your order.`);
            document.getElementById('orderForm').reset();
            document.getElementById('fileInput').value = '';
            document.getElementById('fileName').textContent = '';
            document.getElementById('uploadBtn').textContent = 'Choose File';
            document.getElementById('uploadBtn').classList.remove('remove');
            resetMaterialSelection();
            scrollToSection('track');
        } else {
            let errorMessage = 'Error submitting order:\n';
            if (data.errors) {
                for (let field in data.errors) {
                    errorMessage += `${field.charAt(0).toUpperCase() + field.slice(1)}: ${data.errors[field].join(', ')}\n`;
                }
            } else {
                errorMessage += data.message || 'Unknown error occurred.';
            }
            alert(errorMessage);
        }
    })
    .catch(error => {
        console.error('Fetch Error:', error);
        alert('Error submitting order: ' + error.message);
    });
}

function trackOrder() {
    const receiptCode = document.getElementById('track-receipt-code').value;
    if (!receiptCode || !/^\d{8}$/.test(receiptCode)) {
      document.getElementById('track-result').textContent = 'Please enter a valid 8-digit Receipt Code.';
      return;
    }
    const baseUrl = "{% url 'track_order' 'PLACEHOLDER' %}".replace("PLACEHOLDER", receiptCode);
    window.location.href = baseUrl;
}