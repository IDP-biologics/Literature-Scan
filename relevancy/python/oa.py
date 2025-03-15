import xml.etree.ElementTree as ET
import sys, os
import requests
from time import sleep
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def get_oa_xml(pmc_id):
    sleep(1)
    # Construct the URL
    base_url = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"
    url = f"{base_url}?id={pmc_id}"
    
    # Download the file
    output_file = f"{pmc_id}.xml"
    wget_command = f'wget -O {output_file} "{url}"'
    
    # Execute wget command and check return code
    return_code = os.system(wget_command)
    if return_code != 0:
        raise Exception(f"Failed to download XML file for PMC ID: {pmc_id}. wget returned code {return_code}")
    
    # Verify file exists and is not empty
    if not os.path.exists(output_file):
        raise Exception(f"Failed to create output file: {output_file}")
    
    if os.path.getsize(output_file) == 0:
        os.remove(output_file)  # Clean up empty file
        raise Exception(f"Downloaded file is empty: {output_file}")
    
    return output_file

def parse_oa_response(filename):
    sleep(1)
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Find the PDF link in the records
        pdf_link = root.find('.//link[@format="pdf"]')
        
        if pdf_link is not None:
            # Get the href attribute which contains the FTP URL
            pdf_url = pdf_link.get('href')
            
            # Extract the PMC ID from the record
            pmc_id = root.find('.//record').get('id')
            
            # Construct the wget command
            wget_command = f'wget -O {pmc_id}.pdf "{pdf_url}"'
            print(wget_command)
            os.system(wget_command)
        else:
            print("No PDF link found in the response")
            
    except ET.ParseError:
        print("Error: Invalid XML file")
    except Exception as e:
        print(f"Error: {str(e)}")

def get_pdf(pmcid):
    get_oa_xml(pmcid)
    parse_oa_response(f"{pmcid}.xml")

if __name__ == "__main__":
    with open("pdfs.txt", "r") as f:
        for line in f:
            pmcid = line.strip()
            get_oa_xml(pmcid)
            sleep(1)
            #get_pdf(pmcid)