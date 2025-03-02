import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("..")

from LLMConfig import LLMConfig
from PDFSummarizer import PDFSummarizer

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_file>")
        sys.exit(1)

    config = LLMConfig()
    print(f"{config}")
    summarizer = PDFSummarizer(config)
    
    # Extract and summarize PDF
    pdf_path = sys.argv[1]
    if len(sys.argv) > 2:
        term = sys.argv[2]
    else:
        term = None
    
    summarizer.extract_text(pdf_path)
    print("\nInitial Summary:")
    print(summarizer.summarize())
    
    # Interactive question loop
    print("\nEnter questions about the document (or 'quit' to exit):")
    while True:
        question = input("\nQuestion: ").strip()
        if question.lower() == 'quit':
            break
        print("\nAnswer:")
        print(summarizer.ask_question(question))
    
    # Save conversation when exiting
    output_file = summarizer.save_conversation()
    print(f"\nConversation saved to: {output_file}")

if __name__ == "__main__":
    main()
