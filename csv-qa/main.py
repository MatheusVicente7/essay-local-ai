import streamlit
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
	load_dotenv()
	streamlit.set_page_config(page_title= " Ask your csv")
	streamlit.header("Ask your CSV")

	user_csv = streamlit.file_uploader("Upload your csv", type = "csv")
	if user_csv is not None:
		user_question = streamlit.text_input("Question")

		llm = OpenAI(temperature=0.2)
		#Agents can run code by itself and  be dangerous to the file
		#Agents can aswell utilises external tools, like google and pandas
		agent = create_csv_agent(llm, user_csv,verbose = True)

		if user_question is not None and user_question != "":
			response = agent.run(user_question)
			streamlit.write(response)
if __name__ == "__main__":
    main()
