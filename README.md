# Creating-Knowledge-Graph-from-Text-file

## Knowledge Graph :

A knowledge graph is a structured representation of information that connects entities and their relationships. It's essentially a semantic network where nodes represent entities (like people, places, things, or concepts) and edges represent the relationships between them (like "is_a", "has_part", "located_at").

Key characteristics of a knowledge graph:

Entities: The basic building blocks of a knowledge graph. They can be concrete objects (e.g., people, places, things) or abstract concepts (e.g., ideas, theories).
Relationships: The connections between entities. They describe how entities are related to each other (e.g., "is_a", "has_part", "located_at").
Properties: Additional information associated with entities or relationships (e.g., attributes, values).
How knowledge graphs are used:

Question Answering: Knowledge graphs can be used to answer complex questions by following the relationships between entities.
Recommendation Systems: By analyzing the relationships between entities, knowledge graphs can recommend relevant items to users.
Semantic Search: Knowledge graphs can improve search results by understanding the semantic meaning of queries and returning more relevant results.
Data Integration: Knowledge graphs can be used to integrate data from multiple sources and provide a unified view of information.
Examples of knowledge graphs:

Google Knowledge Graph: Used by Google Search to provide more informative and relevant search results.

DBpedia: A knowledge graph extracted from Wikipedia data.

Freebase: A large-scale knowledge graph developed by Google.

Implementation : 

Step1 : Create the example folder structure with the respective files : 

a. app.py : It is the executable file locally run through streamlit 

b. entity_relationship_extraction.py : The logic for entity relationship extraction , which LLM to leverage and parsing llm response content 

c. visualize_graph.py : It has the definition of how the knowledge graph should look like 

d. newyork.txt and raw_text.txt : This are sample .txt file which are used to create knowledge graph feel free to update with your specific .txt file and point to it .

Step 2 : Update the files 

Update your OPEN AI Key and choice of model in entity_relationship_extraction.py . In model i considered "gpt-4o-mini" , you can update with your choice .

client = OpenAI(api_key="OPEN AI - API KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
  )

Point to the .txt file of choice in app.py

text_file_path = "newyork.txt"

Step 3 : run the requirements.txt file ( command : pip install -r requirements.txt

Step 4 : run the streamlit app locally ( command : streamlit run app.py )

Visually you will see the following components : 

1. Section 1 : It will highlight the extracted entities , a partial snapshot below .
   ![image](https://github.com/user-attachments/assets/dd88fb63-24f5-49ce-8aad-b2e089d5dc85)

2. Section 2 : It highlights the Extracted relationship tuples , a partial snapshot below .
   ![image](https://github.com/user-attachments/assets/e31f6f79-d847-4745-a620-2ce9ddf4ac30)

3. Section 3 : Visualization of the knowledge graph .
   ![image](https://github.com/user-attachments/assets/ab1b4cc5-5a09-4bca-8018-2142717620d5)

   Happy coding :)






