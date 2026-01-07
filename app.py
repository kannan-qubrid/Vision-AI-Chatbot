"""
Visual AI - Chat Interface
Clean minimal UI - ready for redesign.
"""
import streamlit as st
from PIL import Image
import time
from datetime import datetime
from typing import Dict, Any

from backend.chain import VisionChain
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from frontend.ui_components import render_sidebar
from frontend.base_config import get_base_css

# Page configuration
st.set_page_config(
    page_title="Visual AI",
    page_icon="💬",
    layout="wide"
)

# Apply global design constraints
st.markdown(get_base_css(), unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if "conversations" not in st.session_state:
        st.session_state.conversations = {}
    
    if "active_conversation_id" not in st.session_state:
        st.session_state.active_conversation_id = None
    
    if "chat_memory" not in st.session_state:
        st.session_state.chat_memory = InMemoryChatMessageHistory()
    
    if "vision_chain" not in st.session_state:
        st.session_state.vision_chain = VisionChain(st.session_state.chat_memory)

    if "last_uploaded_image_name" not in st.session_state:
        st.session_state.last_uploaded_image_name = None


def create_conversation(image: Image.Image, image_name: str) -> str:
    """Create a new conversation."""
    conversation_id = f"conv_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    st.session_state.conversations[conversation_id] = {
        "title": image_name,
        "image": image,
        "image_name": image_name,
        "messages": [],
        "created_at": datetime.now().isoformat()
    }
    
    return conversation_id


def switch_conversation(conversation_id: str):
    """Switch to a different conversation and rebuild LangChain memory."""
    if conversation_id not in st.session_state.conversations:
        return
    
    st.session_state.active_conversation_id = conversation_id
    st.session_state.chat_memory.clear()
    
    conversation = st.session_state.conversations[conversation_id]
    for msg in conversation["messages"]:
        if isinstance(msg, HumanMessage):
            st.session_state.chat_memory.add_user_message(msg.content)
        elif isinstance(msg, AIMessage):
            st.session_state.chat_memory.add_ai_message(msg.content)


def add_message_to_conversation(role: str, content: str):
    """
    Add message to active conversation (UI storage only).
    IMPORTANT: Does NOT touch LangChain memory.
    """
    if not st.session_state.active_conversation_id:
        return
    
    if role == "human":
        message = HumanMessage(content=content)
    else:
        message = AIMessage(content=content)
    
    conversation = st.session_state.conversations[st.session_state.active_conversation_id]
    conversation["messages"].append(message)
    
    # Update title with first user message
    if role == "human" and len(conversation["messages"]) == 1:
        title_text = content[:27] + ("..." if len(content) > 27 else "")
        conversation["title"] = f"🔍 {title_text}"


def get_active_conversation() -> Dict[str, Any]:
    """Get the currently active conversation."""
    if not st.session_state.active_conversation_id:
        return None
    return st.session_state.conversations.get(st.session_state.active_conversation_id)


def main():
    """Main chat application logic."""
    initialize_session_state()
    
    # Handle conversation switching from sidebar
    if "switch_to_conversation" in st.session_state:
        conv_id = st.session_state.switch_to_conversation
        switch_conversation(conv_id)
        del st.session_state.switch_to_conversation
    
    # Chat App Bar (State 2: After "New Chat")
    # Only show when user is in chat view (not landing)
    st.markdown("""
        <div style="margin-bottom: 2rem;">
            <h1 style="
                font-size: 42px;
                font-weight: 600;
                line-height: 1.2;
                margin: 0;
                padding: 0;
                color: #000000;
            ">Visual AI Chat</h1>
            <p style="
                font-size: 24px;
                font-weight: 400;
                line-height: 1.5;
                margin: 4px 0 0 0;
                padding: 0;
                color: #666666;
            ">Ask questions about your images using advanced vision AI</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Render sidebar and get model config
    model_config = render_sidebar()
    
    st.divider()
    
    # Image upload section
    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"],
        help="Upload an image to analyze"
    )
    
    # Handle image upload
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Only create new conversation if different image
        if st.session_state.last_uploaded_image_name != uploaded_file.name:
            conversation_id = create_conversation(image, uploaded_file.name)
            switch_conversation(conversation_id)
            
            st.session_state.last_uploaded_image_name = uploaded_file.name
            st.success(f"New conversation: {uploaded_file.name}")

    
    st.divider()
    
    # Main chat area
    active_conv = get_active_conversation()
    
    if active_conv:
        # Display image
        st.image(active_conv["image"], width="stretch")
        
        st.divider()
        
        # Display messages
        for message in active_conv["messages"]:
            if message.type == "human":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(message.content)
            elif message.type == "ai":
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(message.content)
        
        # Chat input
        user_query = st.chat_input("Ask about the image...")
        
        if user_query:
            # Add user message
            add_message_to_conversation("human", user_query)
            
            with st.chat_message("user", avatar="👤"):
                st.markdown(user_query)
            
            # Get AI response
            with st.chat_message("assistant", avatar="🤖"):
                message_placeholder = st.empty()
                
                try:
                    response = st.session_state.vision_chain.stream(
                        image=active_conv["image"],
                        user_query=user_query,
                        temperature=model_config.get("temperature", 0.7),
                        max_tokens=model_config.get("max_tokens", 1024),
                        top_p=model_config.get("top_p", 0.9),
                        top_k=model_config.get("top_k", 40),
                        presence_penalty=model_config.get("presence_penalty", 0.0)
                    )
                    
                    full_response = ""
                    chunk_buffer = ""
                    
                    for chunk in response:
                        chunk_buffer += chunk
                        
                        if len(chunk_buffer) >= 3:
                            full_response += chunk_buffer
                            message_placeholder.markdown(full_response + "▌")
                            chunk_buffer = ""
                            time.sleep(0.02)
                    
                    if chunk_buffer:
                        full_response += chunk_buffer
                    
                    message_placeholder.markdown(full_response)
                    
                    add_message_to_conversation("ai", full_response)
                    st.rerun()
                
                except Exception as e:
                    message_placeholder.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
