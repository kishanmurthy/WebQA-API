# <img src="https://raw.githubusercontent.com/kishanmurthy/WebQA-Extension/main/images/main_128.png" alt= “Logo” width="45" height="45">  WebQA-API 

![Screenshot 2023-05-04 at 2 18 31 AM](https://user-images.githubusercontent.com/25534697/236163239-7b4bb04e-bc58-43f3-b342-b5b39b0ac051.png)

WebQA project allows a user to ask any question on the contents of the webpage using LangChain, OpenAI Embeddings and gpt-3.5-turbo. The project consist of
- <b>WebQA-Extension</b> - Chrome Extension
- <b>WebQA-API</b> - Flask API

WebQA-API is a comprehensive solution that offers a cutting-edge question-answer endpoint. It processes incoming JSON post requests containing webpage data and user questions. The API starts by chunking down the webpage data and requesting embeddings from OpenAI. The obtained embeddings and chunked document is then temporarily stored in Chroma vector store.

The API also obtains the question's embedding and employs embedding nearest search to find relevant documents. A specialized prompt is then crafted using the obtained documents and user question, and it's sent to OpenAI API via langchain. Once OpenAI API responds, the WebQA-API forwards the response to form an accurate response to the user.





