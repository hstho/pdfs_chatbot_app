def handle_userinput(user_question, conversation_chain):
    response = conversation_chain({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    #get source text chunks
    st.session_state.source_text_chunks = response.get("source_documents", [])

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
            # Display source text chunk after bot response
            if i//2 < len(st.session_state.source_text_chunks):
                st.write(f"Source text: {st.session_state.source_text_chunks[i//2]}")
            else:
                st.write("No source text available for this response.")


def handle_userinput(user_question, conversation_chain):
    response = conversation_chain({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    #get source text chunks
    st.session_state.source_text_chunks = response["source_documents"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
            # Display source text chunk after bot response
            st.write(f"Source text: {st.session_state.source_text_chunks[i//2]}")