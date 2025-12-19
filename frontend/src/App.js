import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
  if (!message.trim()) return;

  // Add user message
  setMessages((prev) => [...prev, { role: "user", text: message }]);
  setLoading(true);

  try {
    const res = await fetch("https://weather-ai-backend.onrender.com/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!res.ok) {
      throw new Error("Server error");
    }

    const data = await res.json();

    // Add AI response
    setMessages((prev) => [...prev, { role: "ai", text: data.reply }]);
  } catch (error) {
    // Handle backend / network errors
    setMessages((prev) => [
      ...prev,
      { role: "ai", text: "⚠️ Server error. Please try again later." },
    ]);
  } finally {
    setLoading(false);
    setMessage("");
  }
};


  return (
    <div className="app">
      <div className="chat-card">
        <h2> Weather AI Assistant</h2>

        <div className="chat-box">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`chat-message ${msg.role}`}
            >
              {msg.text}
            </div>
          ))}

          {loading && <div className="chat-message ai">Thinking...</div>}
        </div>

        <input
          type="text"
          placeholder="Ask about weather..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
