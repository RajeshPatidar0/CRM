// FORM SUBMIT (Log Interaction)

document.getElementById("interactionForm").addEventListener("submit", async function(e){

e.preventDefault()

const data = {

hcp_name: document.getElementById("hcp").value,
interaction_type: document.getElementById("type").value,
date: document.getElementById("date").value,
time: document.getElementById("time").value,
attendees: document.getElementById("attendees").value,
topics: document.getElementById("topics").value,
sentiment: document.getElementById("sentiment").value,
outcome: document.getElementById("outcome").value,
followup: document.getElementById("followup").value

}

const res = await fetch("http://127.0.0.1:8000/log-interaction",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

})

const result = await res.json()

alert(result.message)

})



/* AI ASSISTANT CHAT */

document.getElementById("chatBtn").addEventListener("click", async function(){

const text = document.getElementById("chatText").value

if(text === ""){

alert("Please write interaction first")

return

}

const res = await fetch("http://127.0.0.1:8000/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:text
})

})

const data = await res.json()

document.getElementById("chatBox").innerText = data.response

})


document.getElementById("chatBtn").addEventListener("click", async () => {

const text = document.getElementById("chatText").value

const res = await fetch("http://127.0.0.1:8000/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
message:text
})
})

const data = await res.json()

const ai = JSON.parse(data.response)

document.getElementById("hcp").value = ai.hcp_name
document.getElementById("type").value = ai.interaction_type
document.getElementById("topics").value = ai.topics
document.getElementById("sentiment").value = ai.sentiment
document.getElementById("outcome").value = ai.outcome
document.getElementById("followup").value = ai.followup

})



document.getElementById("chatBtn").addEventListener("click", async () => {

const text = document.getElementById("chatText").value

const chatBox = document.getElementById("chatBox")

// user message
chatBox.innerHTML += `<div class="user-msg">${text}</div>`

const res = await fetch("http://127.0.0.1:8000/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:text})
})

const data = await res.json()

// AI message
chatBox.innerHTML += `<div class="ai-msg">${data.response}</div>`

chatBox.scrollTop = chatBox.scrollHeight

})

