import gradio as gr
import os
from groq import Groq


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def greet(name):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Me dê uma palavra legal para cada letra presente no nome: {name}",
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content

demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
)

demo.launch(share=True)
