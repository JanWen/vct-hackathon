import './App.css'
//prov
import { ThemeProvider } from "@/components/theme-provider"
//comp
import MessagesContainer from '@/components/ui/MessagesContainer'
import { ModeToggle } from "@/components/ui/mode-toggle"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
//icon
import { AIOutlineSend } from "@/components/ui/icons/AIOutlineSend"
import { useState } from 'react'

let messageData = [];
function App() {
  const [messages, setmessages] = useState([]);

  const keyUpHandler = (pEvent) => {
    if (pEvent.keyCode !== 13) {
      return;
    }
    handleClick();
  }
  
  const sendMessage = async (pMessage) => {
    const response = await fetch(window.location.origin + "/converse", {
      method: "POST",
      body: JSON.stringify(messageData),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    });
    let message = await response.text();
    // prevStateArray => [...prevStateArray, newValue]
    setmessages(prevMessages => [...prevMessages, ["assistant", message]]);
    messageData.push(["assistant", message])
  }

  const handleClick = () => {
    let input = document.querySelector(".message-input").value;
    
    setmessages(prevMessages => [...prevMessages, ["user", input]]); 
    messageData.push(["user", input]);
    document.querySelector(".message-input").value = "";
    sendMessage(input);
  }
  return (
    <>
      <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <ModeToggle></ModeToggle>
        <MessagesContainer messages={messages}/>
        <div className="send-container">
          <Input className="message-input" placeholder='Type your message...' onKeyUp={keyUpHandler}/>
          <Button className="message-send" onClick={handleClick}><AIOutlineSend /></Button>
        </div>
      </ThemeProvider>
    </>
  )
}

export default App
