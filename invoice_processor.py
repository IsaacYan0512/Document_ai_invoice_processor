from typing import Optional
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore
import requests

class DocumentAIProcessor:
    def __init__(self, processor_name, url):
        self.url = url
        self.location = "us"
        self.mime_type = "application/pdf"
        self.field_mask = "text,entities,pages.pageNumber"
        self.project_id = "dojobnow"

        if processor_name.lower() == "expense":
            ## replace dojobnow processor id
            self.processor_id = "dff6f0f2295529f6"
            ## replace dojobnow processor version id
            self.processor_version_id = "pretrained-expense-v1.4-2022-11-18"
        elif processor_name.lower() == "invoice":
            ## replace dojobnow processor id
            self.processor_id = "270d6fc513c422a6"
            ## replace dojobnow processor id
            self.processor_version_id = "pretrained-invoice-v2.0-2023-12-06"
        else:
            raise ValueError("Unsupported processor name. Please use 'expense' or 'invoice'.")

    @staticmethod
    def download_file_from_url(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    def extract_fields(self, document):
        fields = {}
        for entity in document.entities:
            field_name = entity.type_
            field_value = entity.mention_text
            if entity.normalized_value:
                field_value = entity.normalized_value.text
            if field_name in fields:
                if not isinstance(fields[field_name], list):
                    fields[field_name] = [fields[field_name]]
                fields[field_name].append(field_value)
            else:
                fields[field_name] = field_value
        return fields

    def process_document(self):
        file_data = self.download_file_from_url(self.url)
        opts = ClientOptions(api_endpoint=f"{self.location}-documentai.googleapis.com")
        client = documentai.DocumentProcessorServiceClient(client_options=opts)

        name = client.processor_version_path(
            self.project_id, self.location, self.processor_id, self.processor_version_id
        )

        raw_document = documentai.RawDocument(content=file_data, mime_type=self.mime_type)
        process_options = documentai.ProcessOptions(
            individual_page_selector=documentai.ProcessOptions.IndividualPageSelector(pages=[1])
        )

        request = documentai.ProcessRequest(
            name=name,
            raw_document=raw_document,
            field_mask=self.field_mask,
            process_options=process_options,
        )

        result = client.process_document(request=request)
        document = result.document
        document_fields = self.extract_fields(document)
        print("JSON document fields:", document_fields)

# Usage example:
processor_expense = DocumentAIProcessor("expense", "https://cdn-au-dev.dojobnow.io/20240416/d206734c-3cb2-47d4-b29e-e7263239fffc.pdf")
processor_expense.process_document()

processor_invoice = DocumentAIProcessor("invoice", "https://cdn-au-dev.dojobnow.io/20240416/d206734c-3cb2-47d4-b29e-e7263239fffc.pdf")
processor_invoice.process_document()
