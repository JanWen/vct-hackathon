function MessagesContainer(props) {
    let messages = props.messages;
    let counter = 0;
    return (
        <>
            <div className="messages">
                {messages.map((message) => (
                    <div key={counter++} className={"message-" + (message.isSent ? "sent" : "received")}>{message.text}</div>
                ))}
            </div>
        </>
    )
}

export default MessagesContainer