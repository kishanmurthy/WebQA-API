# <img src="https://raw.githubusercontent.com/kishanmurthy/WebQA-Extension/main/images/main_128.png" alt= “Logo” width="45" height="45">  WebQA-API 

![Screenshot 2023-05-04 at 2 18 31 AM](https://user-images.githubusercontent.com/25534697/236163239-7b4bb04e-bc58-43f3-b342-b5b39b0ac051.png)

WebQA project allows you to ask any question on the contents of the webpage using LangChain, OpenAI Embeddings and gpt-3.5-turbo. The project consist of
- [<b>WebQA-Extension</b>](https://github.com/kishanmurthy/WebQA-Extension/) (Chrome Extension)
- <b>WebQA-API</b> (Python Flask API)

WebQA-API offers a cutting-edge question-answer endpoint for webpages. It processes incoming JSON post requests containing webpage data and user questions. The API initially starts by chunking down the webpage data and requesting embeddings from OpenAI. The obtained embeddings and chunked webpage documents are then temporarily stored in Chroma embedding DB.

The API also obtains the question's embedding and employs embedding nearest search to find relevant documents. A specialized prompt is then crafted using the obtained documents and user questions, and it's sent to OpenAI API via LangChain. Once OpenAI API responds, the WebQA-API forwards the response to form an accurate response to the user.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install WebQA-API.

```bash
pip install -r requirements.txt
```

## Usage

### Configuring OpenAI API Key

WebQA-API requires OpenAI API key to be configured in the ```src/config.py``` file. 

```python
OPENAI_API_KEY = "YOUR_API_KEY"
```

### Running WebQA-API

WebQA-API can be run locally using the following command.

```bash
python app.py
```

## API Endpoints

WebQA-API offers the ```/question-answer``` endpoint that takens in json POST request in the following format.

```json
{
    "webpage": "CONTENT OF THE WEBPAGE",
    "question": "QUESTION TO BE ASKED"
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](
https://choosealicense.com/licenses/mit/)
