# Automation-in-Python
Section 1

Hands-on Build Tools to Automate Stuff in Python

Hacker News Headlines Email

- Introduction to Web Scraping
- Setting up the Environment
- Project Architecture Overview
- Building the Hacker News Scraper
- Sending Email from Python
- Building the Headlines Email Module

Project Architecture Overview

Hacker News Headlines Email
- GET HN Website Front Page
- Scrape Required Content(Title/Link)
- Build Email Body/Content
- Email Authentication
- Email Sent

Packages that will be used:
- request
- bs4
- smtplib(default)
- email.mime(default)
- datetime(default)

Section 2

TED Talk Downloader

- Installation and Introduction to requests package
- Building the basic script to download the video
- Generalising the script to get arguments
- Packaging the script as a CLI tool

Section 3

Table Extractor from PDF

- Basics of PDF File Format
  The general structure of a PDF file is composed of the following code components:
  - Header - contains just one line that identifies the version of PDF
  - Body - contains all the object information - Font, Images, Words, Bookmarks from Field and so on
  - Cross-Reference(xref) table contains pointer to all the objects included in the PDF file.
    Its identifies how many objects are in the table
  - Trailer - contains pointers to the xref table and to key objects contained in the trailer dictionary. 
    It ends with %%EOF to identify end of file
  
- Installing required Python modules
- Extracting Table from PDF
- Introducing to Pandas DataFrame
- Writing Table into a CSV

Libraries

- Camelot
  - give the power to tweak table extraction
  - bad tables can be discarded based on Metrics like accuracy and whitespace,
  without ever having to manually look at each table
  - each table is a Pandas DataFrame, which seamlessly integrated into ETL and Data Analysis Workflows
  - export to multiples formats, including JSON, Excel and HTML
- Tabula
- Pdfplumber
- Pdftable
- Pdf-table-extract

Section 4

Automated Bulk Resume Parser

Going through Resumes and extracting relevant information before hiring new resources
 
Automated bulk resume parser can go through multiple resumes and extract relevant information from them and
convert them into a structured tabular format.

Natural Language Processing using Spacy

Libraries

- import pdfminer-pdf to text
- import spacy-nlp
- import re-regex
- import os-os file path
- import pandas as pd- output csv

In resume folder are all pdfs that need to be parsed
In output folder are two sub folders: txt(all converted text from resumes), 
and csv(all structured data from the txt folder)
One important file that we need is pdftxt.py . The file is present in PDF miner library lokated in
https://github.com/pdfminer/pdfminer.six in tools section