import streamlit as st
import ollama

st.title("🧠 AI Coding & Debugging Assistant (Tanpa Internet)")

# Ganti dengan model Ollama khusus coding (pastikan sudah di-pull)
model_name = "codellama:7b"  # Bisa diganti sesuai model coding lain yang kamu pakai

# Inisialisasi chat dan sistem prompt
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a software engineer and expert debugging assistant."
                "Your task is to help users understand, fix, and improve their code."
                "Always provide clear explanations and suggest appropriate fixes or solutions. "
            )
        }
    ]

# Tampilkan riwayat chat sebelumnya
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# Input pengguna
query = st.chat_input("Contoh: Apa bug di kode ini? [tempelkan kode Python Anda]")

if query:
    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        response_stream = ollama.chat(
            model=model_name,
            messages=st.session_state.messages,
            stream=True
        )
        answer = ""
        response_placeholder = st.empty()
        for chunk in response_stream:
            content = chunk.get("message", {}).get("content", "")
            answer += content
            response_placeholder.markdown(answer)
    
    # Simpan ke chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.chat_history.append((query, answer))
