import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the fine-tuned model and tokenizer
model_path = "./fine_tuned_gpt2"  # Path to your fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)
model.eval()  # Set the model to evaluation mode

# Define the app layout
app.layout = html.Div([
    html.H1("Presidential Speech Generator"),
    html.Label("Enter President Name:"),
    dcc.Input(id='president-input', type='text', placeholder='e.g., Abraham Lincoln', debounce=True),
    html.Label("Enter Topic:"),
    dcc.Input(id='topic-input', type='text', placeholder='e.g., Freedom', debounce=True),
    html.Button('Generate Speech', id='generate-button'),
    html.Br(),
    html.Div(id='output')
])

# Define the callback for generating the response
@app.callback(
    Output('output', 'children'),
    [Input('generate-button', 'n_clicks')],
    [dash.dependencies.State('president-input', 'value'),
     dash.dependencies.State('topic-input', 'value')]
)
def generate_speech(n_clicks, president, topic):
    if n_clicks is None or not president or not topic:
        return "Please enter a president and a topic to generate a speech."
    
    # Prepare the input text
    input_text = f"{president} on {topic}:"
    
    # Tokenize and generate output
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    with torch.no_grad():
        output = model.generate(input_ids, max_length=300, num_return_sequences=1, temperature=0.9)
    
    # Decode and display the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return html.Pre(generated_text)

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
