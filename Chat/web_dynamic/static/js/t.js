const users = ['User1', 'User2', 'User3'];
const messages = {
  'User1': ["ghh", "mmh"],
  'User2': ["hi", "me too"],
  'User3': ["okay"]
};

document.addEventListener('DOMContentLoaded', function () {
    const usersList = document.querySelector('.users-list');
    const messagesContainer = document.getElementById('messages-container');
    const typingIndicator = document.getElementById('typing-indicator');
  const messageInput = document.getElementById('message-input');
  const fileInput = document.getElementById('file-input');


    // Display users
    users.forEach(user => {
        const userDiv = document.createElement('div');
        userDiv.innerText = user;
        userDiv.addEventListener('click', () => loadMessages(user));
        usersList.appendChild(userDiv);
    });

    // Load initial messages
  loadMessages(users[0]);
    // Function to load and display messages for a user
  function loadMessages(user) {
    messagesContainer.innerHTML = '';
    messages[user].forEach(message => {
      displayMessage(message);
    });
  }

    // Function to display a message in the chat area
  let lastMessageType = null;
  function displayMessage(message, messageType, f) {
  const messageDiv = document.createElement('div');

    if (messageType === 'sent') {
      if (lastMessageType === null) {
        messageDiv.style.marginTop = '10px';
        messageDiv.style.color = 'red';
        lastMessageType = messageType;
      }
    }
    if (messageType === 'image') {
      const reader = new FileReader();
      reader.addEventListener('load', () => {
        const thumbnailElement = document.createElement('img');
        thumbnailElement.src = reader.result;
        thumbnailElement.classList.add('uploaded-image');
        messageDiv.appendChild(thumbnailElement);
});
      reader.readAsDataURL(f);

    }

    const p = document.createElement('p');
    const m = document.createTextNode(message);
    p.appendChild(m);
    messageDiv.appendChild(p);

    messageDiv.classList.add(messageType === 'sent'? 'sent-message' : 'received-message');
    messagesContainer.appendChild(messageDiv);
    window.alert(messageDiv);

  }


      // Function to send a message

  let activeUser = users[0]
  window.sendMessage = function () {
    const message = messageInput.value.trim();

    if (message !== '') {
      messages[activeUser].push(`You: ${message}`);
      displayMessage(`You: ${message}`, 'sent');
      messageInput.value = '';
      }

    const isFile = fileInput.files.length > 0;
    if (isFile) {
      const file = fileInput.files[0];
      displayMessage('Your file:', 'image', file);

    }
  //  if (isFile) {

     // url = fileInput.files[0];
     // displayMessage('Your file:', 'image', url);
  //    isFile = false:
   // }
  }



    // Function to toggle the visibility of the "Send" button based on input field content
  window.toggleSendButton = function () {
    const sendButton = document.getElementById('send-button');
    const messageInput = document.getElementById('message-input');

    const isMessage = messageInput.value.trim() !== '';



    const isFile = fileInput.files.length > 0;


   // ;
    if (isMessage) {
      sendButton.style.display = 'inline-block';
    } else if (isFile) {
      sendButton.style.display = 'inline-block';

    } else {

    sendButton.style.display = 'none';
    }

  }


    // ... (remaining JavaScript)


})

