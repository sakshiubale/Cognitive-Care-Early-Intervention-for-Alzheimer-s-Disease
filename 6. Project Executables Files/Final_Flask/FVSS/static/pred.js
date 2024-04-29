const detectBtn = document.getElementById('detect-btn');
const chooseImagePage = document.getElementById('choose-image-page');
const selectedImagePage = document.getElementById('selected-image-page');
const imageInput = document.getElementById('image-input');
const chooseBtn = document.getElementById('choose-btn');
const selectedImage = document.getElementById('selected-image');
const analyzeBtn = document.getElementById('analyze-btn');
const resultDiv = document.getElementById('result');

    alert("sakshi")

    detectBtn.addEventListener('click', () => {
      chooseImagePage.style.display = 'block';
    });

    chooseBtn.addEventListener('click', () => {
      const file = imageInput.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          selectedImage.src = reader.result;
          chooseImagePage.style.display = 'none';
          selectedImagePage.style.display = 'block';
        };
        reader.readAsDataURL(file);
      }
    });

    analyzeBtn.addEventListener('click', () => {
      // Here, you'll need to add your code to analyze the selected image
      // and display the results in the result div
      
      // Get the prediction result by sending a request to '/predict' endpoint
        fetch('/predict', {
        method: ['POST','GET'],
        body: formData
        })
      
      
    });
