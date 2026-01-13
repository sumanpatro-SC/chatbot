# chatbot
chatbot for rental-management-system

to run the project 
          streamlit run app.py


BASIC QUESTIONS (Easy)

What is a Rental Management System?
What is the main purpose of this project?
Why is rental management important?
Who are the users of this system?
What problem does this system solve?
What is the objective of the project?
What type of application is this?
Is this system web-based or desktop-based?
What platform is used to develop this project?
What is the role of the admin in the system?


PROJECT DETAILS (Medium)

What are the main modules in the Rental Management System?
How does the system manage rental properties?
How does tenant information get stored?
How does the system help property owners?
What features are provided to users?
How does the system reduce manual work?
What data is stored in the database?
What technologies are used in this project?
What programming languages are used?
What framework is used for backend development?


SYSTEM & FUNCTIONALITY (Medium–Hard)

How does the system handle property listings?
How are rental details updated?
How does the system ensure data accuracy?
How does the system improve efficiency?
What are the advantages of this system?
How does the system help in decision making?
What are the limitations of the existing system?
How is the proposed system better than the existing system?
How does the system store and retrieve data?
What type of database is used?

🔹 ADVANCED / VIVA QUESTIONS (High Value)

What security features are included in the system?
How does the system improve user experience?
What are the future enhancements of this project?
How scalable is the Rental Management System?
How can this system be used in real-world scenarios?
What challenges were faced during development?
How does this project benefit property owners and tenants?
What is the conclusion of the project?

🔹 BONUS (Perfect for Chatbot Demo)

Explain the Rental Management System in simple words.
Summarize the project.
What is the scope of this project?
Why did you choose this project?
How does this system help in automation?
What is the main advantage of using this system?
Describe the project workflow.



🏠 Rental Management System PDF Chatbot
This is a simple PDF-based chatbot for your Rental Management System project.
It allows you to ask questions directly from your project PDF using a simple Streamlit frontend.

🔹 Features

Uses only your PDF file (no database required)
Simple search bar + button interface
Answers come directly from the PDF content
Built with Streamlit + LangChain + FAISS + HuggingFace embeddings
Perfect for college project demo & viva


rental-pdf-chatbot/
 ├── app.py                   # Main Python file
 ├── RentalHub.pdf            # Your project PDF
 └── README.md                # Project documentation


Install required libraries:
pip install streamlit langchain_community langchain_text_splitters faiss-cpu pypdf huggingface-hub


🔹 Example Questions to Ask

What is Rental Management System?
Purpose of this project
Modules in the system
Technology used
Advantages of the system
Future enhancements

🔹 Technologies Used

Python – Programming language
Streamlit – Frontend interface
LangChain Community – Document processing
HuggingFace Embeddings – Vector representation of PDF content
FAISS – Vector database for search

🔹 How It Works

PDF is loaded using PyPDFLoader

Text is split into smaller chunks for better processing
HuggingFace embeddings convert text into vectors
FAISS vector store stores chunks for semantic search
User query is converted to a vector and compared to PDF vectors
Most relevant text is returned as chatbot answer

🔹 Future Enhancements

Support multiple PDFs
Add chat history
Improve UI with HTML/CSS
Offline mode (no API required)
