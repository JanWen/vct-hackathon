function MessagesContainer(props) {
    let messages = props.messages;
    let counter = 0;
    return (
        <>
            <div className="messages">
                {messages.map((message) => (
                    <div key={counter++} className={"message-" + (message[0] === "user" ? "sent" : "received")}>{message[1]}</div>
                ))}
            </div>
        </>
    )
}

export default MessagesContainer