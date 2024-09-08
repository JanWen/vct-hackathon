function MessagesContainer(props) {
    let messages = props.messages;
    return (
        <>
            <div className="messages">
                {messages.map((message) => (
                    <div className={"message-" + (message.isSent ? "sent" : "received")}>{message.text}</div>
                ))}
            </div>
        </>
    )
}

export default MessagesContainer