\# GATE Engineering Mathematics Formula API



A simple backend API built with Python and Flask to store, search, and filter 50+ GATE Engineering Mathematics formulas by topic and keyword.



\## Features



\- 📘 Stores 50+ formulas from GATE Engineering Mathematics syllabus  

\- 🔍 Search formulas by keyword  

\- 🧮 Filter formulas by topic (Calculus, Linear Algebra, Probability, etc.)  

\- 📂 Clean JSON-based data structure  

\- 🌐 Simple REST API built using Flask  



\## Installation



Follow these steps to run the project locally:



\### 1. Clone the repository



git clone https://github.com/prashant-gautam-star/gate-maths-formula-app.git



2\. Navigate into the project folder

&nbsp;  cd gate-maths-formula-app



3\. Create a virtual environment

&nbsp;  python -m venv venv

4\. Activate the virtual environment

&nbsp;  venv\\Scripts\\activate

5\. Install required dependencies

&nbsp;  pip install flask



\## Running the API



6\. Start the Flask server with:

&nbsp;  python app.py



The API will run at:



http://127.0.0.1:5000/



Available Endpoints



1\. Get all topics

&nbsp;  /topics

2\. Get all formulas

&nbsp;  /formulas

3\. Filter formulas by topic

&nbsp;  /formulas?topic=Calculus

4\. Search for formulas

&nbsp;  /search?q=determinant

