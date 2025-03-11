from dotenv import load_dotenv
from openai import OpenAI
from mem0 import Memory
import os

from interpreter import interpreter

interpreter.llm.model = "gpt-4o-mini"
interpreter.auto_run = True

# Load environment variables
load_dotenv()

# point this system to the chromadb
config = {"vector_store": {"provider": "chroma", "config": {"collection_name": "agent_v2_collection", "path": "./chroma_db"}}}

openai_client = OpenAI()
memory = Memory.from_config(config)

def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # Retrieve relevant memories
    relevant_memories = memory.search(query=message, user_id=user_id, limit=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
    system_prompt = f".  Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    
    # Generate openai Assistant response
    # response = openai_client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    # assistant_response = response.choices[0].message.content
    
    # Generate openai interpreter response
    interpreter.system_message += system_prompt
    assistant_response = interpreter.chat( message )

    # Create new memories from the conversation
    messages.append({"role": "assistant", "content": assistant_response[ 0 ][ 'content' ]})
    memory.add(messages, user_id=user_id)

    return assistant_response

def main():
    print("Chat with AI (type 'exit' to quit)")
    while True:
        user_input = input("\n\ninput query: ").strip()
        if user_input.lower() == 'exit' or user_input.lower() == 'x' or user_input.lower() == 'q':
            print("Goodbye!")
            break
        print(f"AI: {chat_with_memories(user_input)}")

if __name__ == "__main__":
    main()