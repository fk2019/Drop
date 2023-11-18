//document.addEventListener('DOMContentLoaded', function () {
  function registerUser() {
    console.log('Yess');
    const form = document.getElementById('registrationForm');
    const formData = new FormData(form);

    // Convert form data to JSON
    const jsonData = {};
    formData.forEach((value, key) => {
      jsonData[key] = value;
    });
    // post user
    fetch('http://127.0.0.1:3000/api/v1/users', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify(jsonData),
    }).then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.satus}`);
      }
      return response.json();
    }).then((data) => {
      console.log('Successfull', data);
    }).catch((er) => {
      console.log('Failed', er);
    });
    window.location.href = 'login.html';
  }

//});
