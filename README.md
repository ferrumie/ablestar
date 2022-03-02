# ablestar
## Setting Up
-   Clone the repo and cd into it:

    ```
    git clone https://github.com/ferrumie/ablestar.git
    ```

- Create a virtual enviroment
	```
	python3 -m venv env
	```
- Activate the virtual enviroment:
    - On Linux/Mac:
	    ```
	    source env/bin/activate
	    ```
    -  On Windows:
        ```
	   env/scripts/activate
	    ```
	Feel free to use other tools such as pipenv or virtualenv

-   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt
    ```

-  Make a copy of the .env.sample file in the app folder and rename it to .env and update the variables accordingly:

    ```
        RETRY_NUM=(number of times to retry the api call) defaults to 5
        API_KEY="shopify api key"
        PASSWORD="shopify password"
    ```
- Build up the package using 
    ``` 
    python setup.py install
    ```

The Three Exercises are Packed in Three different folders
- first_exercise
- second_exercise
- third_exercise

### For Exercise One
- The main script is written inside the first_exercise/utils folder
- You can run this with ` python first_exercise/utils/tag_edit.py`
- The tests are written under first_exercise/tests.py
- Tests can be run with ` python -m unittest first_exercise/tests.py`

### For Exercise Two
- The main script is written inside the second_exercise/shopify_feat.py file
- You can run this with ` python second_exercise/shopify_feat.py`
- The tests are written under second_exercise/tests.py
- There is an exceptions.py file where the exceptions are defined
- There is a fixture folder for the product fixtures
- Tests can be run with ` python -m unittest second_exercise/tests.py`

### For Exercise Three
- The main files are written inside the third_exercise/ folder
- For each discussion question there is a markdown file.
- first_question.md, second_question.md, third_question.md

