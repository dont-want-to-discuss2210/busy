```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MR PAGAL 💗</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

*{box-sizing:border-box}
body{margin:0;font-family:Poppins,sans-serif;background:#120b20;color:white;min-height:100vh;overflow:hidden}
body:before{content:"";position:fixed;width:500px;height:500px;background:#ff4fa3;filter:blur(150px);opacity:.18;top:-150px;left:-150px;pointer-events:none}
body:after{content:"";position:fixed;width:400px;height:400px;background:#8b5cf6;filter:blur(150px);opacity:.15;bottom:-150px;right:-100px;pointer-events:none}

.stars{position:fixed;inset:0;pointer-events:none;overflow:hidden}
.star{position:absolute;color:#ffd6f0;animation:twinkle 2s infinite alternate;opacity:.5}
@keyframes twinkle{from{opacity:.15;transform:scale(.8)}to{opacity:.8;transform:scale(1.2)}}

#lockScreen{position:fixed;inset:0;z-index:10;display:flex;justify-content:center;align-items:center;padding:20px;background:rgba(10,5,20,.92);backdrop-filter:blur(15px)}
.lockBox{width:100%;max-width:400px;text-align:center;padding:35px 25px;border-radius:25px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.15);box-shadow:0 0 50px rgba(255,79,163,.12)}
.lockIcon{font-size:50px;margin-bottom:10px;animation:pulse 2s infinite}
@keyframes pulse{50%{transform:scale(1.08)}}
.lockBox h1{margin:5px 0;font-size:25px}
.lockBox p{color:#cfc5d9;font-size:13px}
.step{display:none}.step.active{display:block}
.stepTitle{color:#ff9bc9;font-size:13px;margin:25px 0 15px}
input{width:100%;padding:15px;border-radius:12px;border:1px solid #493653;background:#1c112b;color:white;text-align:center;font-size:18px;letter-spacing:5px;outline:none}
input:focus{border-color:#ff5fa8;box-shadow:0 0 15px rgba(255,95,168,.2)}
button{border:none;cursor:pointer;font-family:inherit}
.unlockBtn{width:100%;margin-top:15px;padding:14px;border-radius:12px;background:linear-gradient(135deg,#ff4f9a,#a855f7);color:white;font-weight:600;font-size:15px;box-shadow:0 5px 20px rgba(255,79,154,.2)}
.error{color:#ff8fb8;font-size:12px;margin-top:12px;min-height:18px}
.progress{display:flex;gap:6px;margin:20px 0}
.progress span{height:4px;flex:1;background:#35233f;border-radius:10px}
.progress span.active{background:#ff5fa8}

#verifiedPopup{display:none;position:fixed;inset:0;z-index:20;justify-content:center;align-items:center;background:rgba(10,5,20,.85);backdrop-filter:blur(10px)}
.popup{text-align:center;padding:35px 30px;border-radius:25px;background:linear-gradient(145deg,#351a43,#1d102b);border:1px solid #ff75b8;box-shadow:0 0 50px rgba(255,79,163,.25);animation:popupIn .5s ease}
@keyframes popupIn{from{transform:scale(.7);opacity:0}to{transform:scale(1);opacity:1}}
.popup .heart{font-size:55px}.popup h2{color:#ff9dca;font-size:22px;margin:10px 0}.popup p{color:#d8c9df;font-size:13px}

#chatApp{display:none;height:100vh;max-width:700px;margin:auto;flex-direction:column;position:relative;z-index:1}
.chatHeader{padding:18px 20px;display:flex;align-items:center;justify-content:space-between;background:rgba(20,10,35,.75);border-bottom:1px solid rgba(255,255,255,.08);backdrop-filter:blur(15px)}
.profile{display:flex;align-items:center;gap:12px}
.avatar{width:45px;height:45px;border-radius:50%;background:linear-gradient(135deg,#ff4f9a,#8b5cf6);display:flex;justify-content:center;align-items:center;font-size:21px;box-shadow:0 0 20px rgba(255,79,163,.2)}
.profile h3{margin:0;font-size:15px}.profile small{color:#9edfbf;font-size:11px}
.lockBtn{background:#2a1839;color:#e8cce3;padding:9px 12px;border-radius:10px;font-size:12px}
.chatArea{flex:1;overflow-y:auto;padding:25px 18px;display:flex;flex-direction:column;gap:12px}
.welcome{text-align:center;color:#bca9c9;font-size:12px;margin:10px 0 20px}
.message{max-width:78%;padding:11px 15px;border-radius:17px;font-size:13px;line-height:1.5;word-wrap:break-word;animation:messageIn .25s ease}
@keyframes messageIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.message.sent{align-self:flex-end;background:linear-gradient(135deg,#ff4f9a,#b04cf0);border-bottom-right-radius:5px}
.message.received{align-self:flex-start;background:#251634;border:1px solid #3c2850;border-bottom-left-radius:5px}
.time{display:block;font-size:9px;opacity:.6;margin-top:4px;text-align:right}
.chatInput{padding:15px;background:rgba(20,10,35,.8);border-top:1px solid rgba(255,255,255,.08);display:flex;gap:10px}
.chatInput input{flex:1;text-align:left;letter-spacing:0;font-size:13px;padding:13px}
.sendBtn{width:50px;border-radius:12px;background:linear-gradient(135deg,#ff4f9a,#a855f7);color:white;font-size:20px}
.empty{text-align:center;color:#a998b5;font-size:12px;margin:auto}
@media(max-width:500px){.chatHeader{padding:15px}.chatArea{padding:20px 12px}.message{max-width:85%}.lockBox{padding:30px 20px}}
</style>
</head>

<body>

<div class="stars" id="stars"></div>

<div id="lockScreen">
  <div class="lockBox">
    <div class="lockIcon">🔐</div>
    <h1>Private Space 💗</h1>
    <p>Only two special people are allowed here.</p>

    <div class="progress">
      <span class="active"></span><span></span><span></span>
    </div>

    <div class="step active" id="step1">
      <div class="stepTitle">🔑 Enter the first passcode</div>
      <input type="password" id="code1" placeholder="••••••" maxlength="6">
      <button class="unlockBtn" onclick="checkStep(1)">Continue 💗</button>
      <div class="error" id="error1"></div>
    </div>

    <div class="step" id="step2">
      <div class="stepTitle">🎂 When is her birthday?</div>
      <input type="password" id="code2" placeholder="••••••" maxlength="6">
      <button class="unlockBtn" onclick="checkStep(2)">Continue 💗</button>
      <div class="error" id="error2"></div>
    </div>

    <div class="step" id="step3">
      <div class="stepTitle">💍 On which date did you collaborate in October?</div>
      <input type="password" id="code3" placeholder="••••••" maxlength="6">
      <button class="unlockBtn" onclick="checkStep(3)">Unlock Our Space 💗</button>
      <div class="error" id="error3"></div>
    </div>
  </div>
</div>

<div id="verifiedPopup">
  <div class="popup">
    <div class="heart">💗</div>
    <h2>MR PAGAL IS VERIFIED ✨</h2>
    <p>Welcome to your little private world.</p>
  </div>
</div>

<div id="chatApp">
  <div class="chatHeader">
    <div class="profile">
      <div class="avatar">💗</div>
      <div>
        <h3>MR PAGAL ✨</h3>
        <small>● Private & Verified</small>
      </div>
    </div>
    <button class="lockBtn" onclick="lockAgain()">🔒 Lock</button>
  </div>

  <div class="chatArea" id="chatArea">
    <div class="welcome">✨ Your private space ✨<br>Messages are saved online.</div>
  </div>

  <div class="chatInput">
    <input type="text" id="messageInput" placeholder="Write something sweet... 💌">
    <button class="sendBtn" onclick="sendMessage()">➤</button>
  </div>
</div>

<script type="module">

/* =========================================
   FIREBASE IMPORTS
========================================= */

import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";

import {
  getAuth,
  signInAnonymously
} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-auth.js";

import {
  getFirestore,
  collection,
  addDoc,
  query,
  orderBy,
  onSnapshot,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-firestore.js";


/* =========================================
   PASSCODES
========================================= */

const PASSCODE_1 = "220208";
const PASSCODE_2 = "100407";
const PASSCODE_3 = "071025";


/* =========================================
   FIREBASE CONFIG
========================================= */

const firebaseConfig = {
  apiKey: "maine nhi bhaji",
  authDomain: "buzy-f42e5.firebaseapp.com",
  projectId: "buzy-f42e5",
  storageBucket: "buzy-f42e5.firebasestorage.app",
  messagingSenderId: "966470789515",
  appId: "1:966470789515:web:27c49a58934cf0c2f0a78e",
  measurementId: "G-45DM8GH4NK"
};


/* =========================================
   INITIALIZE FIREBASE
========================================= */

const app = initializeApp(firebaseConfig);

const auth = getAuth(app);
const db = getFirestore(app);

const messagesRef = collection(db, "mrPagalMessages");


/* =========================================
   ANONYMOUS LOGIN
========================================= */

try {
  await signInAnonymously(auth);
  console.log("Firebase anonymous authentication successful.");
} catch (error) {
  console.error("Firebase authentication error:", error);
}


/* =========================================
   PASSCODE SYSTEM
========================================= */

let currentStep = 1;

window.checkStep = function(step) {

  const input = document.getElementById("code" + step).value;
  const error = document.getElementById("error" + step);

  let correctCode;

  if (step === 1) correctCode = PASSCODE_1;
  if (step === 2) correctCode = PASSCODE_2;
  if (step === 3) correctCode = PASSCODE_3;

  if (input === correctCode) {

    error.textContent = "";

    if (step < 3) {

      document.getElementById("step" + step).classList.remove("active");
      document.getElementById("step" + (step + 1)).classList.add("active");

      document.querySelectorAll(".progress span")[step].classList.add("active");

      currentStep++;

    } else {

      unlockApp();

    }

  } else {

    error.textContent = "Wrong code. Access cancelled. ❌";

    setTimeout(() => location.reload(), 1200);

  }
};


/* =========================================
   UNLOCK APP
========================================= */

function unlockApp() {

  document.getElementById("lockScreen").style.display = "none";
  document.getElementById("verifiedPopup").style.display = "flex";

  setTimeout(() => {

    document.getElementById("verifiedPopup").style.display = "none";
    document.getElementById("chatApp").style.display = "flex";

    loadMessages();

  }, 2200);
}


/* =========================================
   LOCK AGAIN
========================================= */

window.lockAgain = function() {
  location.reload();
};


/* =========================================
   SEND MESSAGE
========================================= */

window.sendMessage = async function() {

  const input = document.getElementById("messageInput");
  const text = input.value.trim();

  if (text === "") return;

  if (!auth.currentUser) {
    alert("Firebase authentication is not ready.");
    return;
  }

  try {

    await addDoc(messagesRef, {

      text: text,

      senderId: auth.currentUser.uid,

      time: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
      }),

      createdAt: serverTimestamp()

    });

    input.value = "";

  } catch (error) {

    alert("Message send nahi hua. Firebase check karo.");
    console.error(error);

  }
};


/* =========================================
   LOAD MESSAGES
========================================= */

function loadMessages() {

  const chatArea = document.getElementById("chatArea");

  const q = query(
    messagesRef,
    orderBy("createdAt", "asc")
  );

  onSnapshot(q, (snapshot) => {

    chatArea.innerHTML = `
      <div class="welcome">
        ✨ Your private space ✨<br>
        Messages are saved online.
      </div>
    `;

    if (snapshot.empty) {

      chatArea.innerHTML += `
        <div class="empty">
          No messages yet...<br>
          Start your little conversation 💌
        </div>
      `;

    }

    snapshot.forEach((doc) => {

      const msg = doc.data();

      const div = document.createElement("div");

      if (msg.senderId === auth.currentUser?.uid) {
        div.className = "message sent";
      } else {
        div.className = "message received";
      }

      const text = document.createElement("span");
      text.textContent = msg.text;

      const time = document.createElement("span");
      time.className = "time";
      time.textContent = msg.time || "";

      div.appendChild(text);
      div.appendChild(time);

      chatArea.appendChild(div);

    });

    chatArea.scrollTop = chatArea.scrollHeight;

  }, (error) => {

    console.error("Firestore error:", error);
    alert("Messages load nahi ho rahe. Firestore Rules check karo.");

  });
}


/* =========================================
   ENTER TO SEND
========================================= */

document.getElementById("messageInput").addEventListener("keydown", function(e) {

  if (e.key === "Enter") {
    sendMessage();
  }

});


/* =========================================
   FLASHING STARS
========================================= */

for (let i = 0; i < 35; i++) {

  const star = document.createElement("div");

  star.className = "star";
  star.innerHTML = "✦";

  star.style.left = Math.random() * 100 + "%";
  star.style.top = Math.random() * 100 + "%";

  star.style.fontSize =
    (Math.random() * 10 + 5) + "px";

  star.style.animationDelay =
    Math.random() * 3 + "s";

  document.getElementById("stars").appendChild(star);

}

</script>

</body>
</html>
```
