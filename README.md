# AI Chat Room with GPT-4Gen
## 1. Introduction
This AI chat room application was created by ChatGPT, a large language model developed by OpenAI, in collaboration with a human user. The purpose of this project is to demonstrate how a user can interact with an AI model to build a simple chat room application using the OpenAI API.

## 2. Design and Functionality
The chat room is designed using the Tkinter library in Python and utilizes the OpenAI Python API (specifically, the `gpt-3.5-turbo` model) to generate responses based on user input. The source code for the chat room can be found in the file `chatroom_gpt4gen.py`.

Key features of the chat room include:

Sending user input to the OpenAI API and receiving AI-generated responses.
Storing the API key in the `OPENAI_API_KEY` environment variable.
Remembering chat history to provide contextual responses.
Clearing the chat history upon receiving the "/clear" command from the user.

## 3. Testing
To test the chat room application, a separate test script called `test_chatroom_gpt4gen.py` has been provided. This script uses Python's built-in `unittest` module to validate the application's behavior.

To run the tests, simply execute the following command in your terminal:

```
python test_chatroom_gpt4gen.py
```

The test script includes test cases for the AI response generation and clearing the chat history. Please note that running the tests will consume API tokens, so be cautious with the number of tests and the frequency of running them.

## 4. Prompts Used
The prompts used during the development of this AI chat room application are translations of the questions and instructions provided by the user during the conversation. They include:

1. [User] 你是python tk 與使用 openai python API (`gpt-3.5-turbo`) 的專家
(Translation: You are an expert in Python Tk and using the OpenAI Python API (gpt-3.5-turbo).)

2. [User] 用英文寫以下python程序: 寫一個聊天室, 規格如下

   - 使用者的輸入可以透過 openai python API (gpt-3.5-turbo) 得到回應
   - openai的API KEY存放在OPENAI_API_KE環境變數
   - openai 必須記住歷史聊天訊息
   - 當使用者的輸入為 "/clear", 清除歷史聊天訊息

(Translation: Write a Python program in English: Create a chat room with the following specifications:
   - User input can get responses through the OpenAI Python API (gpt-3.5-turbo).
   - The OpenAI API key is stored in the OPENAI_API_KEY environment variable.
   - OpenAI must remember the chat history.
   - When the user input is "/clear", clear the chat history.)

3. [User] 根據https://platform.openai.com/docs/api-reference/chat/create, 請用 gpt-3.5-turbo model撰寫
(Translation: According to https://platform.openai.com/docs/api-reference/chat/create, please write using the gpt-3.5-turbo model

4. [User] 請撰寫測試驗證程序
(Translation: Please write a test validation script.)

5. [User] 請用英文撰寫README, 分為四部分: 第一部份寫出你的版本, 並說明這個作者是你和人類一起製作的; 第二部分說明聊天室的設計方法和功能, 並假設聊天室的檔案為"chatroom_gpt4gen.py"; 第三部分說明如何測試, 並假設測試程式檔名為 "test_chatroom_gpt4gen.py"; 第四部份說明我使用的 prompts, 翻譯從本次聊天的第一個prompt到目前prompt(並且包含這個prompt)
(Translation: Please write a README in English, divided into four parts: The first part states your version and explains that the author is you and a human working together; the second part explains the design and functionality of the chat room, assuming the chat room file is "chatroom_gpt4gen.py"; the third part explains how to test, assuming the test program filename is "test_chatroom_gpt4gen.py"; the fourth part explains the prompts I used, translating from the first prompt of this chat to the current prompt (including this prompt).)

The README provided above addresses these prompts and provides the necessary information to understand, use, and test the AI chat room application.