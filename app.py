with gr.Blocks() as ui:

    gr.Markdown("# 🧠 Synthetic Dataset Generator")

    with gr.Row():

        model = gr.Dropdown(
        choices=list(HF_MODELS.keys()),
        value="Qwen 2.5 3B",
        label="LLM Model",
        info="Qwen and Phi provide the most reliable JSON generation."
        )

        prompt_style = gr.Dropdown(
            choices=[
                "Realistic",
                "Creative",
                "Diverse"
            ],
            value="Realistic",
            label="Prompt Style"
        )

    topic = gr.Textbox(
        label="Dataset Topic",
        placeholder="Fitness Studio"
    )

    studio_type = gr.Dropdown(
    choices=[
        "Dance Studio",
        "Gym",
        "Yoga Studio",
        "Pilates Studio",
        "CrossFit Box",
        "Swimming Pool",
        "Martial Arts Studio",
        "Pole Dance",
        "Aerial Acrobatics"
    ],
    label="Studio Type"
)
    studio_style = gr.Dropdown(
    choices=[
        "Luxury",
        "Simple"
    ],
    label="Studio Style"
)

    rows = gr.Slider(
        minimum=5,
        maximum=30,
        value=5,
        step=5,
        label="Number of rows"
    )

    prompt = gr.Textbox(
        lines=6,
        label="Description",
        placeholder="Describe the dataset you want..."
    )

    generate = gr.Button("Generate Dataset")
    output = gr.Dataframe()
    download = gr.File()


    generate.click(fn=generate_data,
    inputs=[
        model,
        prompt_style,
        studio_style,
        studio_type,
        rows,
        prompt,
        topic
    ],
    outputs=[output,download]
    )

if __name__ == "__main__":
    ui.launch(debug=True)
