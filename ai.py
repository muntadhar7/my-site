import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyB0bsLcJscEib6MmcJFbiKpRabbmFChRkI")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
output = response.text
