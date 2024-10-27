from openai import OpenAI

client = OpenAI(api_key="OPEN AI - API KEY")

def extract_entities_relationships(text):
  messages = [
  {"role": "system", "content": """"
  You are a helper tool for a knowedge graph builder application. Your task is to extract entities and relationships from the text provided by the user. 
  Format the output in such a way that it can be directly parsed into Python lists. 
  The format should include:
  
  1. A list of **Entities** in Python list format.
  2. A list of **Relationships**, where each relationship is represented as a tuple in the format: (Entity 1, "Relationship", Entity 2).
  
  Here is the format to follow:
  
  Entities: ["Entity 1", "Entity 2", ..., "Entity N"]
  
  Relationships: [("Entity 1", "Relationship", "Entity 2"), ..., ("Entity X", "Relationship", "Entity Y")]
  
  Example Input:
  Extract entities and relationships from the following text:
  "Michael Jackson, born in Gary, Indiana, was a famous singer known as the King of Pop. He passed away in Los Angeles in 2009."
  
  Expected Output:
  
  Entities: ["Michael Jackson", "Gary, Indiana", "Los Angeles", "singer", "King of Pop", "2009"]
  
  Relationships: [
      ("Michael Jackson", "born in", "Gary, Indiana"), 
      ("Michael Jackson", "profession", "singer"), 
      ("Michael Jackson", "referred to as", "King of Pop"), 
      ("Michael Jackson", "passed away in", "Los Angeles"), 
      ("Michael Jackson", "date of death", "2009")
  ]
  """},
    {"role": "user", "content": f"Extract entities and relationship tuples from the following text:\n\n{text}\n\n"}
  ]
  
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
  )
  response_content = response.choices[0].message.content
  return response_content

import ast

def parse_llm_response_content(content):
    # Split the output into entities and relationships sections
    entity_section = content.split("Entities:")[1].split("Relationships:")[0].strip()
    relationship_section = content.split("Relationships:")[1].strip()

    # Use ast.literal_eval to safely evaluate the string into Python lists
    entities = ast.literal_eval(entity_section)
    relationships = ast.literal_eval(relationship_section)
    
    return entities, relationships

def get_entities_relationships(raw_text):
  content = extract_entities_relationships(raw_text)
  entities, relationships = parse_llm_response_content(content)
  return entities, relationships
  
