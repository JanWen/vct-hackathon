import './App.css'

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { AIOutlineSend } from "@/components/ui/icons/AIOutlineSend"
import MessagesContainer from './MessagesContainer'

import { useState } from 'react'

function App() {
  const [messages, setmessages] = useState([]);

  const keyUpHandler = (pEvent) => {
    if (pEvent.keyCode !== 13) {
      return;
    }
    handleClick();
  }
  
  const sendMessage = async (pMessage) => {
    const response = await fetch("http://127.0.0.1:8000/converse", {
      method: "POST",
      body: JSON.stringify({"text": pMessage}),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    });
    let message = await response.text();
    // prevStateArray => [...prevStateArray, newValue]
    setmessages(prevMessages => [...prevMessages, {text: message, isSent: false}]); 
  }

  const handleClick = () => {
    let input = document.querySelector(".message-input").value;
    
    setmessages(prevMessages => [...prevMessages, {text: input, isSent: true}]); 
    document.querySelector(".message-input").value = "";
    sendMessage(input);
  }
  return (
    <>
      <MessagesContainer messages={messages}/>
      <div className="send-container">
        <Input className="message-input" placeholder='Type your message...' onKeyUp={keyUpHandler}/>
        <Button className="message-send" onClick={handleClick}><AIOutlineSend /></Button>
      </div>
    </>
  )
}

export default App
