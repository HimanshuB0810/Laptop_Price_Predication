### 💻 Laptop Price Prediction
This project is a machine learning model and a web application designed to predict the price of a laptop based on its key specifications. The model is built using the RandomForestRegressor algorithm and deployed as an interactive web application using Streamlit.

### ✨ Features
Interactive Web Interface: A user-friendly Streamlit application allows you to select various laptop specifications from dropdown menus and input fields.

Accurate Predictions: The model, trained on a comprehensive dataset, provides a robust price prediction.

Data-Driven Insights: The core model development is documented in a Jupyter Notebook, showcasing data cleaning, exploratory data analysis (EDA), and feature engineering.

Pre-trained Model: The web app uses a pre-trained machine learning pipeline (pipe.pkl), ensuring quick and efficient predictions without needing to retrain the model.

### 🚀 Technologies Used
Python: The core programming language for the entire project.

Streamlit: Used to create the interactive web application.

Pandas: For data manipulation and analysis.

NumPy: For numerical operations.

scikit-learn: For machine learning preprocessing, model training, and evaluation.

RandomForestRegressor:  The high-performing gradient boosting algorithm used for the final prediction model.

Matplotlib & Seaborn: Used in the Jupyter Notebook for data visualization.

### 📂 Project Structure
app.py: The main Python script for the Streamlit web application.

code.ipynb: A Jupyter Notebook containing the complete machine learning workflow, from data loading to model selection.

requirements.txt: Lists all the Python dependencies required to run the project.

df.pkl: A pickled file of the preprocessed DataFrame, used for populating dropdown menus in the web app.

pipe.pkl: The saved machine learning pipeline object, which includes the data preprocessing steps and the final XGBoost model.

Notebook/: A directory that contains the dataset files used for the model (laptop_data.csv)

### ⚙️ Installation
To set up and run this project on your local machine, follow these steps:

Clone the repository:

git clone <repository_url>
cd laptop_price_predication


Create and activate a virtual environment:
It is highly recommended to use a virtual environment to manage dependencies.

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


Install dependencies:
Install all the required libraries using the requirements.txt file.

pip install -r requirements.txt


Download the pickled files:
The pre-trained model and DataFrame are necessary for the app to run. Ensure df.pkl and pipe.pkl are available in the root directory.

### 🚀 Usage
Once the dependencies are installed, you can launch the Streamlit web app with a simple command.

streamlit run app.py


This will start a local web server and open the application in your default browser. You can then interact with the interface to select a laptop's brand, type, CPU, RAM, storage, GPU, OS, and other features to get a price prediction.

### 🧠 Model & Workflow
The model development process is fully documented in the code.ipynb notebook. The key steps include:

Data Cleaning: Handling categorical and numerical features, and cleaning up inconsistent data formats.

Feature Engineering: Creating new, more predictive features like 'ppi' (pixels per inch) and simplified categories for 'CPU Brand', 'Gpu Brand', and 'OS'.

Model Training: Training and evaluating several regression models on the preprocessed data. The Random Forest Regressor was selected for its superior performance (R2 score of ~0.88).

Log Transformation: The target variable, Price, was log-transformed to address its skewed distribution, which improved model accuracy.

Pipeline: A scikit-learn Pipeline combines the data preprocessing steps and the final model into a single, cohesive object (pipe.pkl) for easy deployment.