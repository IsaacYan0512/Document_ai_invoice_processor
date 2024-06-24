# Document AI Processor

The DocumentAIProcessor script is designed to automatically process PDF documents using Google Cloud's Document AI service. It supports different processing configurations for expense reports and invoices by dynamically setting the processor based on the document type.

## Features

- **Document Processing**: Automatically processes PDF documents for expenses and invoices.
Dynamic Configuration: Adjusts the processor settings based on the document type.
Error Handling: Includes basic error handling to manage common issues like network errors or configuration problems.
- **Dynamic Configuration**: Adjusts the processor settings based on the document type.
- **Error Handling**: Includes basic error handling to manage common issues like network errors or configuration problems.

## Prerequisites

Before you can run the script, you need:

- Python 3.6 or higher.
- Access to Google Cloud services with Document AI API enabled.
- Properly configured Google Cloud credentials.
- The requests library for fetching documents from URLs.

## Install dependencies

```bash
pip install -r requirements.txt
```

# Usage
To use the script, you need to specify the processor name and the URL of the PDF document you want to process. The script can be run directly from the command line.

1. Edit the script to specify the default URLs or pass them dynamically as arguments (if you modify the script to accept command line arguments).

2. Run the script:

```bash
python invoice_processor.py
```
This will process the documents using the specified Document AI processors for expense reports and invoices.

# Configuration
You can configure the script by modifying the following parameters in the `DocumentAIProcessor` class initialization:

 - **processor_name**: "expense" or "invoice" to specify the type of document.
 - **url**: URL of the PDF document to process.


## Setting up a service account for authentication

In order to securely and automatically use the Document AI service, you need to authenticate with a service account. The following steps will guide you through creating a service account and configuring your environment.

### Create a service account

1. Log in to [Google Cloud Console](https://console.cloud.google.com/).
2. Select or create a project and go to **IAM and Administration** > **Service Accounts**.
3. Click **Create Service Account**, enter an account name and description, and click **Create**.
4. At the **Grant access to this service account** stage, select the appropriate role, such as `Document AI API User`.
5. Click **Finish** to create the service account.

## Create and download the private key

1. In the list of service accounts, locate the service account you just created and click on it.
2. Go to the **Keys** tab, click **Add Key**, and select **Create New Key**. 3.
3. Select **JSON** as the key type and click **Create**. The key file will be downloaded to your computer, which is your private key for accessing the GCP service.

## Document AI Processor

## Directory structure

```bash
documentai_processor/
├── Dockerfile
├── dojobnow-7c20292f1eec.json
├── invoice_processor.py
├── requirements.txt
└── README.md
```

## Prerequisites

Before you begin, make sure you have completed the following steps:

1. Create a Google Cloud project:

   - Create a project in the Google Cloud Console.
      1. Click on the My First Project drop-down list and select New Project in the top right corner of the pop-up window.
            ![Alt text](image.png)
      2. Enable the Document AI API:

         - Select the project you just created.
         - Click on the "Navigation Menu" button in the top left corner and select "APIs and Services" > "Libraries".
         - Type "Document AI" in the search field, find "Cloud Document AI API" and click on it.
         - Click the "Enable" button to enable the API.
      3. Configuring a Service Account
         
         - Create a service account:

            Click on the "Navigation Menu" button in the top left corner and select "IAM and Administration" > "Service Accounts".
            Click the "+ Create Service Account" button at the top.
            Enter the Service Account Name and Description and click "Create and Continue".
         
         - Grant permissions:

            On the "Grant this service account access to the project" screen, assign the appropriate roles to the service account. For example, select the Document AI User role.
            Click Continue.
         
         - Create a key:

            On the service account details screen, click the Keys tab at the top, and then click Add Key > Create New Key.
            Select the JSON format and click "Create".
            The JSON file will be automatically downloaded to your computer. Keep this file safe as it contains the private key for your service account.
         
         - Configuring IAM Privileges
         
            Configure IAM permissions:
            Click on the Navigation Menu button in the upper left corner and select IAM and Administration > IAM.
            Locate the service account you just created and click the "Edit Members" button to the right of the service account.
            
            In the "Add Roles" section, search for and add the following roles:
               Document AI User
               Viewer or other appropriate role
            
            When finished, click "Save".

   - Create a service account and download the key file in JSON format, place it in the project directory.

3. install requirements

   ```bash
      pip install google-cloud-documentai requests
   ```

2. requirements.txt

   This file lists the Python packages needed for the project.

   ```bash
   google-cloud-documentai
   requests
   ```

3. invoice_processor.py

   ```bash
      if processor_name.lower() == "expense":
               self.processor_id = "dff6f0f2295529f6"
               self.processor_version_id = "pretrained-expense-v1.4-2022-11-18"
      elif processor_name.lower() == "invoice":
         self.processor_id = "270d6fc513c422a6"
         self.processor_version_id = "pretrained-invoice-v2.0-2023-12-06"
   ```
   This part contains the ids and version ids of both processors.



   ```bash
      processor_expense = DocumentAIProcessor("expense", "https://cdn-au-dev.dojobnow.io/20240416/d206734c-3cb2-47d4-b29e-e7263239fffc.pdf")
      processor_expense.process_document()

      processor_invoice = DocumentAIProcessor("invoice", "https://cdn-au-dev.dojobnow.io/20240416/d206734c-3cb2-47d4-b29e-e7263239fffc.pdf")
      processor_invoice.process_document()
   ```

   This part points to the storage address of the expense and invoice used for the demo.