const users = ['Winnie Ryder', 'User2', 'User3'];
const apiUrl = 'http://127.0.0.1:3000/api/v1/users';
fetch(apiUrl).then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
}).then((data) => {
  console.log(data);
}).catch((er) => {
  console.log(er);
});
const messages = {
  'Winnie Ryder': ["Midnight green is a relatively dark, green-bluish color. It’s the official primary color of the Philadelphia Eagles, which is why it’s also sometimes referred to as eagle green.", "mmh"],
  'User2': ["hi", "me too"],
  'User3': ["okay"]
};
const avatars = {
  'Winnie Ryder': '../static/images/avatars/smiling_lady4.png',
  'User2': '../static/images/avatars/smiling_man.png',
  'User3': '../static/images/avatars/smiling_lady3.png'
};

document.addEventListener('DOMContentLoaded', function () {
    const usersList = document.querySelector('.users-list');
    const messagesContainer = document.getElementById('messages-container');
    const typingIndicator = document.getElementById('typing-indicator');
  const messageInput = document.getElementById('message-input');
  const fileInput = document.getElementById('file-input');
  const header = document.querySelector('.chat-header');
  const sideBar = document.querySelector('.side-bar');
  const userPic = document.createElement('div');
  const userP = document.createElement('p');
  const userHeader = document.querySelector('.user-header');
  const socket = io();
  socket.connect('http:127.0.0.1:5000');
  function loadUserImage(user, el, userPicDiv, userPar) {
    const url = avatars[user];
    const userImage = document.createElement('img');
    userPicDiv.innerHTML = '';
    userPar.innerHTML = '';
    userPicDiv.classList.add('user-pic');
    userPar.classList.add('user-name');
    userPicDiv.appendChild(userImage);
    userImage.src = url;
    const userName = document.createTextNode(user);
    userPar.appendChild(userName);

    el.appendChild(userPicDiv);
    el.appendChild(userPar);
  }

  function displayHeader(user, el, userPicDiv, userPar) {
    if (userPicDiv && userPar) {
      const userDiv = document.createElement('div');
      loadUserImage(user, userDiv, userPicDiv, userPar);
      el.appendChild(userDiv);
    } else {
      const userPic = document.createElement('div');
      const userP = document.createElement('p');
      loadUserImage(user, el, userPic, userP);
    }
  }

    // Display users
  users.forEach(user => {
    const userDiv = document.createElement('div');
    userDiv.addEventListener('click', () => loadMessages(user));

    displayHeader(user, userDiv);
    usersList.appendChild(userDiv);
  });


  loadMessages(users[0]);
    // Function to load and display messages for a user
  function loadMessages(user) {
    userHeader.innerHTML = '';
    messagesContainer.innerHTML = '';
    displayHeader(user, userHeader, userPic, userP);
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
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }


      // Function to send a message

  let activeUser = users[0]
  window.sendMessage = function () {
    const message = messageInput.value.trim();

    if (message !== '') {
      messages[activeUser].push(`You: ${message}`);
      displayMessage(`You: ${message}`, 'sent');
      socket.emit('message', message);
      messageInput.value = '';
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }

    const isFile = fileInput.files.length > 0;
    if (isFile) {
      const file = fileInput.files[0];
      displayMessage('', 'image', file);

    }

  }

  window.toggleSendButton = function () {
    const sendButton = document.getElementById('send-button');
    const messageInput = document.getElementById('message-input');

    const isMessage = messageInput.value.trim() !== '';



    const isFile = fileInput.files.length > 0;


    if (isMessage) {
      sendButton.style.display = 'inline-block';
    } else if (isFile) {
      sendButton.style.display = 'inline-block';

    } else {

    sendButton.style.display = 'none';
    }

  }

})
