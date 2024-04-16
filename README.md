# [Text To SQL](https://www.youtube.com/watch?v=wFdFLWc-W4k&t=488s)

Here the [Youtube videos](https://www.youtube.com/watch?v=wFdFLWc-W4k)

The agenda is to conver the text into SQL application.

Prompt--->LLM--->GRmini Pro--->Query--->SQL Database--->Response


Implementation

1. SQLlite --> Insert some Recods --> Pyton Programing
2. LLM Application--->gemini Pro--->SQL Database.


## local setup
### Step 1
Create a `virtual environment` and activate
```cmd
python -m venv venv
```
windows
```cmd
source venv/Scripts/activate
```
linux
```cmd
source venv/bin/activate
```

### Step 2
Install the all the `requirements.txt`
```cmd
pip install -r requirements
```

### Step 3
create a `.env` file and set this variable
```cmd
GOOGLE_API_KEY=<MY_GOOGLE_API_KEY>
```
### Step 4 Run Streamlit APP
```cmd
streamlit run app.py
```
