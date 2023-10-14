# Opposable Thumbs - Forensics Challenge

## Basic Information
**Name:** Opposable Thumbs  
**Category:** Forensics  
**Points:** 50

## Objective

The "Opposable Thumbs" challenge is a forensics task that involves examining a downloaded file to uncover hidden information. Your objective is to discover the flag concealed within this file.

## Solution

To successfully complete the "Opposable Thumbs" forensics challenge, follow these steps:

1. **Analyze the Downloaded File:**
   - Start by examining the downloaded file. At first glance, it might seem undetectable or unremarkable.

2. **Hexadecimal Analysis:**
   - Open the file using a hexadecimal editor or hex viewer (hexedit) to explore its content. During this analysis, you may come across pieces of "IHDR" and "IEND" markers, which are typically found in image files. These markers suggest that there are hidden items or images within the file.

3. **Attempt Binwalk:**
   - Initially, you may attempt to use Binwalk with the `-e` option to extract any embedded items or files from the main file. However, if Binwalk doesn't yield any results, you'll need to explore alternative methods.

4. **Use Foremost:**
   - Utilize a tool like Foremost, which specializes in carving and extracting files from various data formats. Perform a forensic analysis of the file using Foremost to extract hidden content.

5. **Browse Extracted Images:**
   - After running Foremost, you will likely obtain a set of extracted images and files. Browse through these extracted items, paying close attention to the images.

6. **Locate and Decode the Flag:**
   - Within the extracted images, you should eventually find the flag. 

Flag: flag{XXXXXXXXXX}

**Challenge Solved**  
